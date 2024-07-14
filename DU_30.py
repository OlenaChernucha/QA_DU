
class Book:

    def __init__(self, title, author, year_publication):
        self.__title = title
        self.__author = author
        self.__year_publication = year_publication
        self.__status = True

    def book_borrow(self):
        if self.__status:
            self.__status = False
            print(f"The book {self.title}' is published")
        else:
            print(f"The book '{self.title}' is no longer available")

    def book_free(self):        
        self.status = True
        print(f"The book '{self.title}' is returned")
           
class User:
    def __init__(self, id_user, name):
        self.__id_user = id_user
        self.__name = name
        self.__books_list = []

    def list_books(self, book):
        self.__book_list.append(book)
        print(f"The book'{book._Book__title}' has been added to your borrowed books")
         
    
    def returned_books(self, book):
        if book in self.__books_list:
            self.__books_list.remove(book)
            print(f"The book '{book._Book__title}' has been removed from your borrowed books")
        else:
            print("You don't have this book borrowed")

class Librarian(User):
    def add_book_catalog(self, book, catalog):
        catalog.append(book)
        print(f"The book '{book._Book__title}' has is been added to the catalog")

    def remove_book_catalog(self, book, catalog):
        if book in catalog:
            catalog.remove(book)
            print(f"The book '{book._Book__title}' has been removed from the catalog")
        else:
            print("The book is not in the catalog")

    def register_user(self, user, users):
        users.append(user)
        print(f"The user '{user._User__name}' has been registered")

    def delete_user(self, user, users):
        if user in users:
            users.remove(user)
            print(f"The user '{user._User__name}' has ben deleted")
        else:
            print(f"The user is not registered")

class Library:
    def __init__(self):
        self.__catalog = []
        self.__users = []

    def book_lend(self, book, user):
        if book in self.__catalog:
            user.add_book(book)
        else:
            print("The book is not available in the library")

    def book_back(self, book, user):
        user.remove_book(book)

    def books_print(self):
        print("Books in the library: ")
        for book in self.__catalog:
            print(book._Book__title)

    def users_print(self):
        print("Library user: ")
        for user in self.__users:
            print(user._User__name)




    
        