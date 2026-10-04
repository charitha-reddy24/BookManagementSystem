CREATE DATABASE bookdb;

USE bookdb;

CREATE TABLE books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    author VARCHAR(100),
    price DECIMAL(10,2)
);

select * from books;