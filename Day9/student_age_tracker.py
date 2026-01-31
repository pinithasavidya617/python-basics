details = []

def add_data(name, age):
    new_data = {name : age}
    details.append(new_data)
    return details

def search_data(detail_list, name):
    for detail in detail_list:
        if name in detail:
            return detail[name]
    return None


def main():
    print("""
    1. Add data
    2. Search data""")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        input_name = input("Enter the name: ")
        input_age = input("Enter the age: ")
        print(add_data(input_name, input_age))
    elif choice == 2:
        input_name = input("Enter the name: ")
        search = search_data(details, input_name)
        print(search)



while True:
    main()