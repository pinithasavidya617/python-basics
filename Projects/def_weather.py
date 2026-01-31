import time

temps_per_week = [[0.0 for _ in range(3)] for _ in range(7)]


def date_input():
    date = int(input("Which day? 1-7:"))
    return date

def hour_input():
    hour = int(input("Which hour? 1-3: "))
    return hour

def add_temperature():
    day = date_input()
    hour = hour_input()
    temp_input = float(input("Input the temperature in celcius: "))

    temps_per_week[day - 1][hour - 1] = temp_input

    for temperatures in temps_per_week:
        time.sleep(0.1)
        print(temperatures)

def show_temperature():
    day = date_input()
    hour = hour_input()
    print(f"Temperature for day {day} , hour {hour} is: {temps_per_week[day - 1][hour - 1]}c")

def average_of_day():
    day = date_input()
    average = sum(temps_per_week[day - 1]) / len(temps_per_week[day - 1])
    print(f"Average of temperatures in day{day} is {average}c")

def highest_temp():
    day = date_input()
    maximum_temp = max(temps_per_week[day - 1])
    temps_per_day = temps_per_week[day - 1]
    print(f"Maximum temperature of day{day} is {maximum_temp}c at {temps_per_day.index(maximum_temp) + 1} hour")

def average_week():
     tot = 0
     for day in temps_per_week:
         for hour in day:
             tot += hour
     print(f"Average temperature of the week is {tot / 21}c")

def exiting():
    print("Exiting...")
    time.sleep(1)


def main():
    while True:
         print("MENU")
         print(""" 
     1.Add Temperature
     2.Show Temperature
     3.Average of Temperatures in a Day
     4.Highest Temperature For a Day
     5.Average of Temperatures of the Week
     6.Exit""")

         which_item = int(input("Enter the number of process: "))
         if which_item == 1:
             add_temperature()
         elif which_item == 2:
             show_temperature()
         elif which_item == 3:
             average_of_day()
         elif which_item == 4:
             highest_temp()
         elif which_item == 5:
             average_week()
         elif which_item == 6:
             exiting()
             break
         else:
             print("Try another number!")
             time.sleep(1)
             continue


main()