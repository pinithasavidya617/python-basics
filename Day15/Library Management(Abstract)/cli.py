from service import LibraryService, LibraryError
from repositories import InMemoryMemberRepository, InMemoryBookRepository, InMemoryLoanRepository

library_service = LibraryService(books=InMemoryBookRepository(),
                                 members= InMemoryMemberRepository(),
                                 loans=InMemoryLoanRepository())


def list_books():
    try:
        books = library_service.list_all_books()
        for book in books:
            status = "Available" if book.is_available() else f"Out by - {book.book_lend_member_id} "
            print(f"Book_id - {book.book_id} | Title - {book.title} | Author - {book.author} | Year - {book.year} |Status - {status}")

    except LibraryError as e:
        print(e)
        return

def add_book():

    book_id = input("Enter book id: ")
    title = input("Enter book title: ")
    author = input("Enter autor of book: ")
    year = input("Enter year: ")

    try:
        library_service.add_book(book_id, title, author, year)
        print(f"{title} added successfully!")

    except LibraryError as e:
        print(e)
        return

def add_member():
    member_id = input("Enter member id: ")
    name = input("Neter member name: ")
    try:
        library_service.register_member(member_id, name)
        print(f" Member: {name} added successfully!")
    except LibraryError as e:
        print(e)
        return

def borrow():
    book_id = input("Enter book id: ")
    member_id = input("Enter member id: ")
    loan_id = input("Enter loan id: ")
    try:
        library_service.borrow_book(loan_id, book_id, member_id)
        books = library_service.list_all_books()

        for book in books:
            print(f" {book.title} book is borrowed by member: {member_id}.")

    except LibraryError as e:
        print(e)
        return

def return_book():

    loan_id = input("Enter loan id: ")
    try:
        library_service.return_book(loan_id)
        print(f"Book with loan ID: {loan_id} returned successfully!")

    except LibraryError as e:
        print(e)
        return

def list_loans():
    loans = library_service.list_all_loans()
    for loan in loans:
        print(f" Loan: {loan.loan_id} | Book: {loan.book_id} | Member: {loan.member_id} | Borrowed at: {loan.borrowed_at}")


while True: #presentation layer
    print("""
    1. List Books
    2. Add Books
    3. Add member
    4. Borrow Book
    5. Return Book
    6. List Loans
    7. Exit""")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        list_books()

    elif choice == 2:
        add_book()

    elif choice == 3:
        add_member()

    elif choice == 4:
        borrow()

    elif choice == 5:
        return_book()

    elif choice == 6:
        list_loans()

    elif choice == 7:
        print("Thank you for using Library System!")
        break

    else:
        print("Enter a valid choice!")

#Repository = CREATE and STORE (CRUD operations)
# Service = VALIDATE and COMPLEX BUSINESS STUFF

# Service Layer = Use ABSTRACT classes (interfaces)
# CLI Layer = Use CONCRETE classes (actual implementations)