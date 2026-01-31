contact_list = {}

def add_to_contact_list(phone_book, name, phone_no):
    if name in phone_book:
        phone_book[name].append(phone_no)
    else:
        phone_book[name] = [phone_no]
    return phone_book

def search_contact(phone_book, name):
    if name in phone_book:
        return f"{name} -> {phone_book[name]}"
    else:
        return "Name unavailable"


def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        return print( f"Contact of {name} is removed. ")
    else:
        return "Name unavailable"


def view_contact(phone_book):
    for key,val in phone_book.items():
        print(f"{key} -> {val}")

def menu():
    print(""" 
    1. Add a New Contact :
    2. Search a Contact :
    3. Delete a Contact :
    4. View Contacts : 
        """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone_no = int(input("Enter the phone number: "))

        add_to_contact_list(phone_book=contact_list,name= name,phone_no= phone_no)
        print(contact_list)

    elif choice == 2:
         name = input("Search name: ")
         print(search_contact(phone_book=contact_list, name=name))

    elif choice == 3:
         if len(contact_list) != 0:
             name =  input("Search name: ")
             delete_contact(phone_book=contact_list,name= name)
         else:
             print("Phonebook is empty! ")
    elif choice == 4:
        view_contact(contact_list)



while True:
    menu()