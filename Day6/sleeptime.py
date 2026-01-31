tot = 0
sleep_hours = []

for i in range(7):
    sleep_input = float(input("How much time did you sleep in hours?"))
    sleep_hours.append(sleep_input)


print(f"Average sleep time : {sum(sleep_hours) / len(sleep_hours)}")

more_than_8 = [hours for hours in sleep_hours if hours > 8]
print(f"Days slept more than 8 hours: {len(more_than_8)}")


# for hours in sleep_hours:
#     if hours > 8:
#         more_than_8.append(hours)




