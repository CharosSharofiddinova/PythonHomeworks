class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    MAX_BORROWED_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum number of books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author):
        book = Book(title, author)
        self.books[title] = book

    def add_member(self, name):
        member = Member(name)
        self.members[name] = member

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"Book '{book_title}' not found in library.")
        if member_name not in self.members:
            raise ValueError(f"Member '{member_name}' not found.")
        member = self.members[member_name]
        book = self.books[book_title]
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            raise ValueError(f"Member '{member_name}' not found.")
        if book_title not in self.books:
            raise BookNotFoundException(f"Book '{book_title}' not found in library.")
        member = self.members[member_name]
        book = self.books[book_title]
        member.return_book(book)

    def display_books(self):
        for book in self.books.values():
            print(book)

    def display_members(self):
        for member in self.members.values():
            print(member)

library = Library()

library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

library.add_member("Alice")
library.add_member("Bob")

try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Alice", "Moby Dick")  # This should raise BookNotFoundException
except Exception as e:
    print(e)
try:
    library.borrow_book("Bob", "1984")  # Should raise BookAlreadyBorrowedException
except Exception as e:
    print(e)
library.return_book("Alice", "1984")
try:
    library.borrow_book("Alice", "1984")
except Exception as e:
    print(e)
print("\nLibrary Books:")
library.display_books()
print("\nLibrary Members:")
library.display_members()
