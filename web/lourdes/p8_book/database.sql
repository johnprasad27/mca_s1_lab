CREATE DATABASE library;
USE library;

CREATE TABLE book (
    edition_no INT PRIMARY KEY,
    title VARCHAR(50),
    authors VARCHAR(100),
    edition VARCHAR(20),
    publisher VARCHAR(50)
);
