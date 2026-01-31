#when user inputs number of minutes, we should output the number of hours and minutes
number_of_minutes = int(input("Enter number of minutes: "))
hours = number_of_minutes // 60
remain_minutes = number_of_minutes % 60 #ex; 90 mins divided by 60 mins mean
print(hours , "hours and", remain_minutes, "minutes")