"""
Neon Runner — an arcade dodge-and-dash game built with pygame

Features
- Slick neon visuals with parallax starfield and particle effects
- Tight controls: move, dash (invincible burst), and slow-mo (bullet time)
- Dynamic difficulty that scales with time
- Power-ups (Shield, Time Shard, Score Orb)
- Screen shake, trails, and juicy hit flashes
- Pause menu, game over screen, and persistent high score (savegame.json)
- Single-file, no external assets required

Controls
- Move: Arrow keys or WASD
- Dash: Left Shift (brief invincibility + burst speed)
- Slow-mo: SPACE (consumes energy, regenerates slowly)
- Pause: P or ESC
- Restart after game over: R
- Quit: Q or close window

Requires: pygame (pip install pygame)

Tested with pygame 2.x
"""
from __future__ import annotations
import math
import os
import json
import random
import time
from dataclasses import dataclass

import pygame

# -------------- Config --------------
WIDTH, HEIGHT = 900, 600
FPS = 60

# Gameplay tuning
PLAYER_SPEED = 320.0
DASH_SPEED = 820.0
DASH_TIME = 0.18
DASH_COOLDOWN = 1.2
INVINCIBLE_AFTER_HIT = 1.2
SLOWMO_SCALE = 0.45
SLOWMO_DRAIN = 0.22  # per second
SLOWMO_REGEN = 0.12  # per second
MAX_SLOWMO = 1.0

ASTEROID_SPAWN_EASY = 0.8   # per second
ASTEROID_SPAWN_HARD = 3.2    # per second
ASTEROID_MIN_SPEED = 120
ASTEROID_MAX_SPEED = 420

ORB_SPAWN = 0.35
POWERUP_SPAWN = 0.08

SHAKE_DECAY = 8.0

SAVEFILE = "savegame.json"

# -------------- Utility --------------

def clamp(v, a, b):
    return max(a, min(b, v))


def lerp(a, b, t):
    return a + (b - a) * t


class Timer:
    def __init__(self):
        self.time = 0.0

    def step(self, dt):
        self.time += dt

    def reset(self):
        self.time = 0.0


# -------------- Visual helpers --------------

def circle_surf(radius, color, glow=0):
    size = radius * 2 + glow * 2
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    center = size // 2
    if glow > 0:
        for i in range(glow, 0, -1):
            alpha = int(255 * (i / glow) ** 2 * 0.18)
            pygame.draw.circle(surf, (*color[:3], alpha), (center, center), radius + i)
    pygame.draw.circle(surf, color, (center, center), radius)
    return surf


def polygon_surf(points, color, glow=0, pad=8):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    w = int(maxx - minx + pad * 2)
    h = int(maxy - miny + pad * 2)
    surf = pygame.Surface((w + glow * 2, h + glow * 2), pygame.SRCALPHA)
    offset = (-minx + pad + glow, -miny + pad + glow)
    if glow > 0:
        for i in range(glow, 0, -1):
            alpha = int(255 * (i / glow) ** 2 * 0.18)
            pygame.draw.polygon(surf, (*color[:3], alpha), [(x+offset[0], y+offset[1]) for x,y in points], width=0)
    pygame.draw.polygon(surf, color, [(x+offset[0], y+offset[1]) for x,y in points])
    return surf, offset


# -------------- Entities --------------
@dataclass
class Particle:
    pos: pygame.Vector2
    vel: pygame.Vector2
    life: float
    color: pygame.Color
    size: float


class ParticleSystem:
    def __init__(self):
        self.ps: list[Particle] = []

    def emit(self, pos, vel, life, color, size):
        self.ps.append(Particle(pygame.Vector2(pos), pygame.Vector2(vel), life, color, size))

    def update(self, dt):
        for p in self.ps:
            p.life -= dt
            p.pos += p.vel * dt
            p.vel *= 0.985
            p.size *= 0.995
        self.ps = [p for p in self.ps if p.life > 0 and 0.5 < p.size < 50]

    def draw(self, surf):
        for p in self.ps:
            alpha = int(255 * clamp(p.life, 0, 1))
            r = max(1, int(p.size))
            s = circle_surf(r, (*p.color[:3], alpha), glow=4)
            surf.blit(s, (p.pos.x - s.get_width()/2, p.pos.y - s.get_height()/2))


class Starfield:
    def __init__(self, count=140):
        self.stars = []
        for _ in range(count):
            layer = random.choice([0.25, 0.5, 1])
            self.stars.append([random.random()*WIDTH, random.random()*HEIGHT, layer])

    def update(self, dt, speed):
        for s in self.stars:
            s[0] -= speed * dt * s[2] * 0.5
            if s[0] < 0:
                s[0] = WIDTH
                s[1] = random.random()*HEIGHT

    def draw(self, surf):
        for x,y,l in self.stars:
            r = 1 if l<0.5 else 2
            c = (180,220,255) if l<1 else (120,190,255)
            surf.fill(c, (int(x), int(y), r, r))


class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.radius = 16
        self.color = pygame.Color(80, 255, 220)
        self.base_surf = circle_surf(self.radius, self.color, glow=10)
        self.trail = ParticleSystem()
        self.alive = True
        self.invincible = 1.0
        self.dash_time = 0.0
        self.dash_cd = 0.0
        self.slowmo = MAX_SLOWMO * 0.75
        self.shield = 0.0
        self.hurt_flash = 0.0

    def update(self, dt, keys, ps: ParticleSystem):
        if not self.alive:
            return
        self.invincible = max(0.0, self.invincible - dt)
        self.hurt_flash = max(0.0, self.hurt_flash - dt)
        self.dash_cd = max(0.0, self.dash_cd - dt)

        move = pygame.Vector2(0,0)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move.x += 1
        if move.length_squared() > 0:
            move = move.normalize()

        speed = PLAYER_SPEED
        if self.dash_time > 0:
            self.dash_time -= dt
            speed = DASH_SPEED
            self.invincible = max(self.invincible, 0.02)  # keep invincible during dash
        self.vel = move * speed
        self.pos += self.vel * dt

        # Keep inside bounds
        self.pos.x = clamp(self.pos.x, self.radius, WIDTH - self.radius)
        self.pos.y = clamp(self.pos.y, self.radius, HEIGHT - self.radius)

        # Trail particles
        if move.length_squared() > 0:
            back = self.pos - move * (self.radius * 0.6)
            for _ in range(2):
                jitter = pygame.Vector2(random.uniform(-20,20), random.uniform(-20,20))
                ps.emit(back + jitter*0.04, -move * random.uniform(40,140), 0.35, pygame.Color(80,255,220), random.uniform(2,4))

        # Slowmo regen
        self.slowmo = clamp(self.slowmo + SLOWMO_REGEN * dt, 0, MAX_SLOWMO)

    def try_dash(self):
        if self.dash_cd == 0.0 and self.dash_time <= 0:
            self.dash_time = DASH_TIME
            self.dash_cd = DASH_COOLDOWN
            return True
        return False

    def take_hit(self):
        if self.invincible > 0:
            return False
        if self.shield > 0:
            self.shield = 0
            self.invincible = INVINCIBLE_AFTER_HIT * 0.5
            self.hurt_flash = 0.2
            return False
        self.alive = False
        self.hurt_flash = 0.6
        return True

    def draw(self, surf):
        s = self.base_surf.copy()
        if self.hurt_flash > 0:
            overlay = pygame.Surface(s.get_size(), pygame.SRCALPHA)
            overlay.fill((255,80,120,int(160*self.hurt_flash)))
            s.blit(overlay,(0,0),special_flags=pygame.BLEND_ADD)
        surf.blit(s, (self.pos.x - s.get_width()/2, self.pos.y - s.get_height()/2))
        if self.shield > 0:
            shield_surf = circle_surf(self.radius+8, (120,220,255,120), glow=8)
            surf.blit(shield_surf, (self.pos.x - shield_surf.get_width()/2, self.pos.y - shield_surf.get_height()/2))


class Asteroid:
    def __init__(self):
        r = random.randint(14, 34)
        self.radius = r
        self.pos = pygame.Vector2(WIDTH + r + 10, random.uniform(r, HEIGHT - r))
        sp = random.uniform(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
        self.vel = pygame.Vector2(-sp, random.uniform(-40,40))
        self.rot = random.uniform(0, math.tau)
        self.rot_speed = random.uniform(-2, 2)
        poly = []
        verts = random.randint(7, 11)
        for i in range(verts):
            ang = i/verts*math.tau + random.uniform(-0.12,0.12)
            rad = r * random.uniform(0.7, 1.15)
            poly.append((math.cos(ang)*rad, math.sin(ang)*rad))
        self.surf, self.offset = polygon_surf(poly, (255,160,110,200), glow=10)

    def update(self, dt):
        self.pos += self.vel * dt
        self.vel.y *= 0.995
        self.rot += self.rot_speed * dt

    def draw(self, surf):
        rotated = pygame.transform.rotozoom(self.surf, -math.degrees(self.rot), 1)
        surf.blit(rotated, (self.pos.x - rotated.get_width()/2, self.pos.y - rotated.get_height()/2))

    def dead(self):
        return self.pos.x < -self.radius - 20 or self.pos.y < -60 or self.pos.y>HEIGHT+60


class Orb:
    def __init__(self):
        self.radius = 10
        self.pos = pygame.Vector2(WIDTH + 20, random.uniform(40, HEIGHT-40))
        self.vel = pygame.Vector2(-random.uniform(150, 260), 0)
        self.color = pygame.Color(255, 235, 120)
        self.surf = circle_surf(self.radius, self.color, glow=8)

    def update(self, dt):
        self.pos += self.vel * dt

    def draw(self, surf):
        surf.blit(self.surf, (self.pos.x - self.surf.get_width()/2, self.pos.y - self.surf.get_height()/2))

    def dead(self):
        return self.pos.x < -30


class PowerUp:
    TYPES = ("shield", "time")
    def __init__(self):
        self.kind = random.choice(PowerUp.TYPES)
        self.radius = 12
        self.pos = pygame.Vector2(WIDTH + 20, random.uniform(50, HEIGHT-50))
        self.vel = pygame.Vector2(-random.uniform(160, 240), 0)
        col = (120,220,255) if self.kind=="shield" else (220,120,255)
        self.surf = circle_surf(self.radius, (*col, 255), glow=10)

    def update(self, dt):
        self.pos += self.vel * dt

    def draw(self, surf):
        surf.blit(self.surf, (self.pos.x - self.surf.get_width()/2, self.pos.y - self.surf.get_height()/2))

    def dead(self):
        return self.pos.x < -30


# -------------- Game --------------
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Neon Runner — Pygame")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 24)
        self.bigfont = pygame.font.SysFont("consolas", 56, bold=True)
        self.smallfont = pygame.font.SysFont("consolas", 18)
        self.reset()

    def reset(self):
        self.player = Player(180, HEIGHT/2)
        self.ps = ParticleSystem()
        self.bg = Starfield(160)
        self.asteroids: list[Asteroid] = []
        self.orbs: list[Orb] = []
        self.powerups: list[PowerUp] = []
        self.score = 0
        self.best = self.load_best()
        self.time_alive = 0.0
        self.spawn_acc = 0.0
        self.orb_acc = 0.0
        self.pow_acc = 0.0
        self.shake = 0.0
        self.paused = False
        self.slowmo_on = False
        self.flash_timer = 0.0

    def difficulty(self):
        t = clamp(self.time_alive/60.0, 0.0, 1.0)
        return lerp(ASTEROID_SPAWN_EASY, ASTEROID_SPAWN_HARD, t)

    def save_best(self):
        try:
            with open(SAVEFILE, "w") as f:
                json.dump({"best": int(self.best)}, f)
        except Exception:
            pass

    def load_best(self):
        if os.path.exists(SAVEFILE):
            try:
                with open(SAVEFILE, "r") as f:
                    return int(json.load(f).get("best", 0))
            except Exception:
                return 0
        return 0

    def aabb_hit(self, a_pos, a_r, b_pos, b_r):
        return (a_pos - b_pos).length_squared() <= (a_r + b_r) ** 2

    def run(self):
        running = True
        while running:
            raw_dt = self.clock.tick(FPS) / 1000.0
            dt = raw_dt
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_p):
                        if self.player.alive:
                            self.paused = not self.paused
                    if not self.player.alive and event.key == pygame.K_r:
                        self.reset()
                    if event.key == pygame.K_q:
                        running = False
            if self.paused:
                self.draw_menu()
                pygame.display.flip()
                continue

            keys = pygame.key.get_pressed()

            # Slow-mo toggle (hold SPACE)
            target_slowmo = 1.0
            if keys[pygame.K_SPACE] and self.player.slowmo > 0.04:
                target_slowmo = SLOWMO_SCALE
                self.player.slowmo = max(0.0, self.player.slowmo - SLOWMO_DRAIN * dt)
                self.slowmo_on = True
            else:
                self.slowmo_on = False
            dt *= lerp(1.0, target_slowmo, 0.85)

            if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and self.player.try_dash():
                self.shake = max(self.shake, 6.0)
                # Dash burst particles
                for i in range(22):
                    ang = random.uniform(0, math.tau)
                    spd = random.uniform(120, 360)
                    self.ps.emit(self.player.pos, (math.cos(ang)*spd, math.sin(ang)*spd), 0.28, pygame.Color(120,255,220), random.uniform(2,3.5))

            if self.player.alive:
                self.time_alive += dt
                self.score += dt * 7.0  # score over time
            else:
                dt *= 0.85

            # Spawning
            self.spawn_acc += dt * self.difficulty()
            while self.spawn_acc >= 1.0:
                self.asteroids.append(Asteroid())
                self.spawn_acc -= 1.0

            self.orb_acc += dt * ORB_SPAWN
            while self.orb_acc >= 1.0:
                self.orbs.append(Orb())
                self.orb_acc -= 1.0

            self.pow_acc += dt * POWERUP_SPAWN
            while self.pow_acc >= 1.0:
                self.powerups.append(PowerUp())
                self.pow_acc -= 1.0

            # Update
            bg_speed = lerp(40, 120, clamp(self.time_alive/60,0,1))
            self.bg.update(dt, bg_speed)
            self.player.update(dt, keys, self.ps)
            for a in self.asteroids:
                a.update(dt)
            for o in self.orbs:
                o.update(dt)
            for p in self.powerups:
                p.update(dt)
            self.ps.update(dt)

            # Collisions
            if self.player.alive:
                for a in self.asteroids:
                    if self.aabb_hit(self.player.pos, self.player.radius, a.pos, a.radius*0.9):
                        if self.player.take_hit():
                            self.shake = max(self.shake, 12.0)
                            self.flash_timer = 0.2
                            self.best = max(self.best, int(self.score))
                            self.save_best()
                        else:
                            self.shake = max(self.shake, 8.0)
                # Orbs
                for o in list(self.orbs):
                    if self.aabb_hit(self.player.pos, self.player.radius, o.pos, o.radius):
                        self.score += 25
                        for i in range(10):
                            ang = random.uniform(0, math.tau)
                            sp = random.uniform(60, 200)
                            self.ps.emit(o.pos, (math.cos(ang)*sp, math.sin(ang)*sp), 0.4, pygame.Color(255,235,120), random.uniform(2,3))
                        self.orbs.remove(o)
                # PowerUps
                for p in list(self.powerups):
                    if self.aabb_hit(self.player.pos, self.player.radius, p.pos, p.radius):
                        if p.kind == "shield":
                            self.player.shield = 1.0
                            self.shake = max(self.shake, 6.0)
                        else:
                            self.player.slowmo = clamp(self.player.slowmo + 0.6, 0, MAX_SLOWMO)
                        for i in range(16):
                            ang = random.uniform(0, math.tau)
                            sp = random.uniform(80, 220)
                            col = (120,220,255) if p.kind=="shield" else (220,120,255)
                            self.ps.emit(p.pos, (math.cos(ang)*sp, math.sin(ang)*sp), 0.42, pygame.Color(*col), random.uniform(2,3))
                        self.powerups.remove(p)

            # Clean up
            self.asteroids = [a for a in self.asteroids if not a.dead()]
            self.orbs = [o for o in self.orbs if not o.dead()]
            self.powerups = [p for p in self.powerups if not p.dead()]

            # Camera shake
            if self.shake > 0:
                self.shake -= SHAKE_DECAY * raw_dt
            if self.flash_timer > 0:
                self.flash_timer -= raw_dt

            # Draw
            self.draw()
            pygame.display.flip()

        pygame.quit()

    # -------------- Draw helpers --------------
    def draw(self):
        # background
        self.screen.fill((8, 10, 18))
        self.bg.draw(self.screen)

        # world surface with shake
        ox = random.uniform(-self.shake, self.shake)
        oy = random.uniform(-self.shake, self.shake)
        world = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        # entities
        for a in self.asteroids:
            a.draw(world)
        for o in self.orbs:
            o.draw(world)
        for p in self.powerups:
            p.draw(world)
        self.player.draw(world)
        self.ps.draw(world)

        self.screen.blit(world, (ox, oy))

        # HUD
        self.draw_hud()

        if self.flash_timer > 0:
            f = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            f.fill((255,140,160,int(160*self.flash_timer)))
            self.screen.blit(f, (0,0), special_flags=pygame.BLEND_ADD)

        if not self.player.alive:
            self.draw_game_over()

    def draw_hud(self):
        # Score & best
        score_s = self.font.render(f"SCORE {int(self.score):06d}", True, (220,240,255))
        best_s = self.font.render(f"BEST  {int(self.best):06d}", True, (150,190,255))
        self.screen.blit(score_s, (20, 16))
        self.screen.blit(best_s, (20, 44))

        # Slow-mo bar
        bar_w, bar_h = 220, 12
        x, y = 20, 74
        pygame.draw.rect(self.screen, (40,50,70), (x-2, y-2, bar_w+4, bar_h+4), border_radius=8)
        fill = int(bar_w * (self.player.slowmo / MAX_SLOWMO))
        pygame.draw.rect(self.screen, (180,160,255), (x, y, fill, bar_h), border_radius=6)
        txt = self.smallfont.render("SLOW-MO", True, (210,200,255))
        self.screen.blit(txt, (x + bar_w + 10, y-3))

        # Dash cooldown dots
        dots = 6
        ready_ratio = 1.0 - (self.player.dash_cd / DASH_COOLDOWN)
        for i in range(dots):
            r = 6
            gap = 4
            cx = 20 + i*(r*2+gap)
            cy = 104
            col = (120,255,220) if (i/dots) < ready_ratio else (40,70,60)
            pygame.draw.circle(self.screen, col, (cx, cy), r)
        label = self.smallfont.render("DASH", True, (160,230,210))
        self.screen.blit(label, (20 + dots*(12+4) + 8, 94))

        # Shield indicator
        if self.player.shield > 0:
            sh = self.smallfont.render("SHIELD", True, (120,220,255))
            self.screen.blit(sh, (20, 124))

        # Hints briefly
        if self.time_alive < 6.0:
            hint = self.smallfont.render("Move: WASD/Arrows  Dash: Shift  Slow-mo: Space  Pause: P", True, (140,180,230))
            self.screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT - 28))

        # Pause banner
        if self.paused:
            p = self.font.render("PAUSED", True, (255,255,255))
            self.screen.blit(p, (WIDTH//2 - p.get_width()//2, 16))

    def draw_menu(self):
        self.screen.fill((8,10,18))
        self.bg.draw(self.screen)
        title = self.bigfont.render("PAUSED", True, (240,250,255))
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 120))
        lines = [
            "Resume: P or ESC",
            "Dash: Shift (invincible burst)",
            "Slow-mo: Space (hold)",
            "Quit: Q",
        ]
        for i, t in enumerate(lines):
            surf = self.font.render(t, True, (190,210,240))
            self.screen.blit(surf, (WIDTH//2 - surf.get_width()//2, HEIGHT//2 - 30 + i*32))

    def draw_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,120))
        self.screen.blit(overlay, (0,0))
        title = self.bigfont.render("GAME OVER", True, (255,225,235))
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 120))
        score = self.font.render(f"Score: {int(self.score)}", True, (220,240,255))
        best = self.font.render(f"Best:  {int(self.best)}", True, (150,190,255))
        self.screen.blit(score, (WIDTH//2 - score.get_width()//2, HEIGHT//2 - 40))
        self.screen.blit(best, (WIDTH//2 - best.get_width()//2, HEIGHT//2 - 8))
        msg = self.smallfont.render("Press R to restart • Q to quit", True, (190,210,240))
        self.screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 + 42))


if __name__ == "__main__":
    Game().run()
