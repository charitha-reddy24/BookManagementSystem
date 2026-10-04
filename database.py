import mysql.connector


class Database:
    def connect(self):
        connection=mysql.connector.connect(host="localhost",port=3307,user="root",password="Charitha@123",database="bookdb")
        return connection

db=Database()
connection = db.connect()


