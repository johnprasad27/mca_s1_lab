CREATE DATABASE university;
USE university;

CREATE TABLE STUDENT(
    Name VARCHAR(10),
    Student_number INT PRIMARY KEY,
    Class INT,
    Major VARCHAR(20)
);

CREATE TABLE COURSE(
    Course_name VARCHAR(30),
    Course_number VARCHAR(20) PRIMARY KEY,
    Credit_hours INT,
    Department VARCHAR(15)
);

CREATE TABLE SECTION(
    Section_identifier INT PRIMARY KEY,
    Course_number VARCHAR(20),
    Semester VARCHAR(10),
    Year INT,
    Instructor VARCHAR(15),
    FOREIGN KEY(Course_number) REFERENCES COURSE(Course_number)
);

CREATE TABLE GRADE_REPORT(
    Student_number INT,
    Section_identifier INT,
    Grade VARCHAR(2),
    PRIMARY KEY(Student_number,Section_identifier),
    FOREIGN KEY(Student_number) REFERENCES STUDENT(Student_number),
    FOREIGN KEY(Section_identifier) REFERENCES SECTION(Section_identifier)
);

CREATE TABLE PREREQUISITE(
    Course_number VARCHAR(20),
    Prerequisite_number VARCHAR(20),
    PRIMARY KEY(Course_number,Prerequisite_number),
    FOREIGN KEY(Course_number) REFERENCES COURSE(Course_number),
    FOREIGN KEY(Prerequisite_number) REFERENCES COURSE(Course_number)
);

-- Courses & grades of Smith
SELECT c.Course_name, g.Grade
FROM STUDENT s
JOIN GRADE_REPORT g ON s.Student_number=g.Student_number
JOIN SECTION se ON g.Section_identifier=se.Section_identifier
JOIN COURSE c ON se.Course_number=c.Course_number
WHERE s.Name='Smith';

-- Students in Database course
SELECT s.Name, g.Grade
FROM STUDENT s
JOIN GRADE_REPORT g ON s.Student_number=g.Student_number
JOIN SECTION se ON g.Section_identifier=se.Section_identifier
JOIN COURSE c ON se.Course_number=c.Course_number
WHERE c.Course_name='Database';

-- Senior students
SELECT Name FROM STUDENT WHERE Class=2;