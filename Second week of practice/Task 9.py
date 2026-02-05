from abc import ABC, abstractmethod


# Абстрактний клас
class Item(ABC):
    @abstractmethod
    def get_info(self):
        pass


# Книга
class Book(Item):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__borrowed = False  # інкапсуляція

    def borrow(self):
        if not self.__borrowed:
            self.__borrowed = True
            return True
        return False

    def return_item(self):
        self.__borrowed = False

    def get_info(self):
        status = "Позичена" if self.__borrowed else "Доступна"
        return f"Книга: {self.title}, Автор: {self.author}, Статус: {status}"


# Читач
class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []

    def take_book(self, book):
        if book.borrow():
            self.books.append(book)
            print(f"{self.name} взяв книгу '{book.title}'")
        else:
            print(f"Книга '{book.title}' вже позичена")

    def return_book(self, book):
        if book in self.books:
            book.return_item()
            self.books.remove(book)
            print(f"{self.name} повернув книгу '{book.title}'")


# Демонстрація взаємодії
book1 = Book("1984", "George Orwell")
book2 = Book("Clean Code", "Robert C. Martin")

reader = Reader("Олександр")

print(book1.get_info())
reader.take_book(book1)
print(book1.get_info())

reader.return_book(book1)
print(book1.get_info())