import time

temps_per_week = [[0.0 for _ in range(3)] for _ in range (7)] #used _(i) because value of it doesn't use anywhere
# for temps_per_day in temps_per_week:
#    print(temps_per_day)


while True:
     print("MENU")
     print(""" 1.Add Temperature
 2.Show Temperature
 3.Average of Temperatures in a Day
 4.Highest Temperature For a Day
 5.Average of Temperatures of the Week
 6.Exit""")

     which_item = int(input("Enter the number of process: "))
     if which_item == 1:
        date_input = int(input("Which day? 1-7:"))
        hour_input = int(input("Which hour? 1-3: "))
        temp_input = float(input("Input the temperature in celcius: "))

        temps_per_week[date_input - 1][hour_input - 1] = temp_input

        for temperatures in temps_per_week:
           time.sleep(0.1)
           print(temperatures)

     elif which_item == 2:
         date_input = int(input("Which day? 1-7:"))
         hour_input = int(input("Which hour? 1-3: "))
         print(f"Temperature for day {date_input} , hour {hour_input} is: {temps_per_week[date_input - 1][hour_input - 1]}c")

     elif which_item == 3:
         date_input = int(input("Which day? 1-7:"))
         average =  sum(temps_per_week[date_input -1]) // len(temps_per_week[date_input -1])
         print(f"Average of temperatures in day{date_input} is {average}c")

     elif which_item == 4:
         date_input = int(input("Which day? 1-7:"))
         maximum_temp =  max(temps_per_week[date_input -1])
         temps_per_day = temps_per_week[date_input -1]
         print(f"Maximum temperature of day{date_input} is {maximum_temp}c at {temps_per_day.index(maximum_temp) + 1} hour")

         # hottest_temp = temps_per_day[0]
         # hootest_day = 0
         #
         # for i in range(len(temps_per_day)):
         #     if temps_per_day[i] > hottest_temp:
         #         hottest_temp = temps_per_day[i]
         #         hootest_day = i
         #
         # print(f"Maximum temperature of day{date_input} is {hottest_temp}c at {hootest_day} hour")


     elif which_item == 5:
         tot = 0
         for day in temps_per_week:
             for hour in day:
                tot += hour
         print(f"Average temperature of the week is {tot / 21}c")

     elif which_item == 6:
         print("Exiting...")
         time.sleep(1)
         break

     else:
         print("Try another number!")
         time.sleep(1)
         continue