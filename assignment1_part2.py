
class Book:

        def __init__(self, title, author):
        self.title = title
        self.author = author

        def display(self):
            print(f"\'{self.title}\', written by {self.author}")

    book1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
    book2= Book(" Walter Scott", "Ivanhoe: A Romance")

    book1.display()
    book2.display()

