#Create three classes Cook Waiter Singer | These classes should have a single method to perform
#their activities
#create robo class and inherit above classes

class Cook:
    def cook(self):
        print("Cooking")

class Waiter:
    def waiter(self):
        print("Serving")

class Singer:
    def singing(self):
        print("Singing")

class Robo(Cook, Waiter, Singer):
    def robo(self):
        print("Robo")

robot = Robo()
robot.cook()
robot.waiter()
robot.singing()
robot.robo()