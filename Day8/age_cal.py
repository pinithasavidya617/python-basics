# take birth year as input
# first write a function to calculate age based on current year and birth year
# if age < 13 return child
# if age<20 return teen
#  if age < 20
#  less than < 50 adult
# age > 50 return senior citizen
# write a function to get age statues based on the age

def cal_age(present, past):
    return present - past

def age_state(age):
    if age <= 13:
        return "Child"
    elif age <= 18:
        return "Teen"
    elif age <= 50:
        return  "Adult"
    else:
        return "Senior Citizen"


def main():
    current_year = int(input("Enter this year: "))
    birth_year = int(input("enter your birth year: "))
    age = cal_age(current_year, birth_year)
    state = age_state(age)
    print(state)


main()
