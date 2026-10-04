from database import Database

class BookManager:
    def __init__(self):
        self.db=Database()

    def close_connection(self, cursor, connection):
        cursor.close()
        connection.close()

    def add_book(self):
        title = input("Enter book title: ")
        while title.strip() == "":
            print("Book title cannot be empty")
            title = input("Enter book title: ")
        author = input("Enter author name: ")
        while not author.replace(" ", "").replace(".", "").isalpha():
            print("Author name cannot be number")
            author = input("Enter author name: ")    
        price=float(input("enter the price: "))
        while price <= 0:
            print("Price must be greater than zero")
            price = float(input("Enter the price: "))
        available_platform = input("Enter available platform: ")
        while available_platform.strip() == "":
            print("Available platform cannot be empty")
            available_platform = input("Enter available platform: ")
        connection=self.db.connect()
        cursor=connection.cursor()
        query="insert into books(title,author,price,available_platform) values(%s,%s,%s,%s)"
        values = (title,author,price,available_platform)
        cursor.execute(query,values)
        connection.commit()
        print("Book added successfully")
        self.close_connection(cursor, connection)

                          
    def view_books(self):
        connection = self.db.connect()
        cursor = connection.cursor()
        query = "select * from books"
        cursor.execute(query)
        books = cursor.fetchall()
        for book in books:
              book = list(book)
              book[3] = float(book[3])
              print(tuple(book))
        self.close_connection(cursor, connection)


    def update_book(self):
        book_id = int(input("Enter the book id to update: "))
        connection = self.db.connect()
        cursor = connection.cursor()
        check_query = "select * from books where id=%s"
        cursor.execute(check_query, (book_id,))
        book = cursor.fetchone()
        if book is None:
            print("Book not found")
        else:
            print("1. Update Title")
            print("2. Update Author")
            print("3. Update Price")
            print("4. Update Available Platform")
            choice = input("Enter your choice: ")
            if choice == "1":
                value = input("Enter new title: ")
                column = "title"
            elif choice == "2":
                value = input("Enter new author: ")
                column = "author"
            elif choice == "3":
                value = float(input("Enter new price: "))
                column = "price"
            elif choice == "4":
                value = input("Enter new available platform: ")
                column = "available_platform"
            else:
                print("Invalid choice")
                cursor.close()
                connection.close()
                return
            query = f"update books set {column}=%s where id=%s"
            cursor.execute(query, (value, book_id))
            connection.commit()
            print("Book updated successfully")
        self.close_connection(cursor, connection)
   
    def delete_book(self):
        book_id = int(input("enter the book id: "))
        connection = self.db.connect()
        cursor = connection.cursor()
        query = "delete from books where id=%s"
        values = (book_id,)
        cursor.execute(query,values)
        if cursor.rowcount > 0:
         connection.commit()
         print("Book deleted successfully")
        else:
            print("Book not found")
        self.close_connection(cursor, connection)


manager = BookManager()

manager.add_book()
manager.view_books()
manager.delete_book()
manager.update_book()