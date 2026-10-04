class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

book1=Book("python","Guido",500)
print(book1.title)
print(book1.author)
print(book1.price)
