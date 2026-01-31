from datetime import datetime
from dataclasses import dataclass
from models import Book, Member, Loan
from repositories import BookRepository, MemberRepository, LoanRepository

class LibraryError(Exception):
    pass

@dataclass
class LibraryService:
 
    books: BookRepository
    loans: LoanRepository
    members: MemberRepository

    def add_book(self, book_id:str, title:str, author:str, year:str) -> Book:
        if self.books.get_by_id(book_id) is not None:
            raise LibraryError(f"Book already exists with book id - {book_id}")

        book = Book(book_id = book_id, title = title, author = author, year = year)
        self.books.add(book) #saves to InMemoryBookRepository
        return book

    def register_member(self, member_id:str, name:str) -> Member:
        if self.members.get_by_id(member_id) is not None:
            raise LibraryError(f"Member already exists with member id - {member_id}")

        member = Member(member_id, name)
        self.members.add(member)
        return member

    def list_all_books(self):
        if len(self.books.list_all_books()) == 0:
            raise LibraryError("No books in the list to show!")

        return self.books.list_all_books()

    def borrow_book(self, loan_id:str, book_id:str, member_id:str) -> Loan:
        if self.books.get_by_id(book_id) is None:
            raise LibraryError(f"Book not found!")

        if self.members.get_by_id(member_id) is None:
            raise LibraryError(f"Member not found!")

        if not self.books.get_by_id(book_id).is_available():
            raise LibraryError(f"Book not available!")

        loan = Loan(loan_id, member_id, book_id, borrowed_at= datetime.now())

        book = self.books.get_by_id(book_id) #Gets the Book object from the repository
        book.book_lend_member_id = member_id #Assigns the borrowing member's ID to the book (marking it as "lent to this member")

        self.books.update(book)

        self.loans.add(loan)
        return loan

    def return_book(self, loan_id: str):

        loan = self.loans.get_by_id(loan_id) #returns loan object

        if loan is None:
            raise LibraryError("Loan doesn't exist!")

        if not loan.is_active():
            raise LibraryError("Loan is not active!") #already returned the book

        book = self.books.get_by_id(loan.book_id) #Gets the actual Book object using the book ID from the loan record
        book.book_lend_member_id = None #This is the key line that "frees" the book
        self.books.update(book)

        loan.returned_at = datetime.now()
        self.loans.update(loan)
        return loan

    def list_all_loans(self):
        return [loan for loan in self.loans.list_all_loans() if loan.is_active()]


