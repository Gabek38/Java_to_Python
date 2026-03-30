# library_demo.py
# Reversed-engineered Python version of the Java LibraryDemo project

class LibraryItem:
    """Base class representing a general library item."""

    def __init__(self, title, item_id):
        self.__title = title
        self.__item_id = item_id
        self.__checked_out = False

    def get_title(self):
        return self.__title

    def get_item_id(self):
        return self.__item_id

    def is_checked_out(self):
        return self.__checked_out

    def check_out(self):
        if not self.__checked_out:
            self.__checked_out = True
            return True
        return False

    def return_item(self):
        if self.__checked_out:
            self.__checked_out = False
            return True
        return False

    def __str__(self):
        return (f"Title: {self.__title}\n"
                f"Item ID: {self.__item_id}\n"
                f"Checked Out: {self.__checked_out}")


class Book(LibraryItem):
    """Subclass representing a book in the library."""

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.__author = author

    def get_author(self):
        return self.__author

    def __str__(self):
        return super().__str__() + f"\nAuthor: {self.__author}"


class DVD(LibraryItem):
    """Subclass representing a DVD in the library."""

    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def __str__(self):
        return super().__str__() + f"\nDuration: {self.__duration} minutes"


# ---- Main driver -----
if __name__ == "__main__":
    book1 = Book("The Hobbit", "B101", "J.R.R. Tolkien")
    dvd1 = DVD("Inception", "D202", 148)

    print("Book Information:")
    print(book1)
    print()

    print("DVD Information:")
    print(dvd1)
    print()

    if book1.check_out():
        print(f"{book1.get_title()} has been checked out.")
    else:
        print(f"{book1.get_title()} is already checked out.")

    if book1.check_out():
        print(f"{book1.get_title()} has been checked out.")
    else:
        print(f"{book1.get_title()} is already checked out.")

    if book1.return_item():
        print(f"{book1.get_title()} has been returned.")
    else:
        print(f"{book1.get_title()} was not checked out.")

    print()

    if dvd1.check_out():
        print(f"{dvd1.get_title()} has been checked out.")
    else:
        print(f"{dvd1.get_title()} is already checked out.")

    print()
    print("Updated DVD Information:")
    print(dvd1)