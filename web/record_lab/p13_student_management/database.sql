CREATE DATABASE mca23;
USE mca23;

CREATE TABLE teacher (
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    PRIMARY KEY (username)
);

INSERT INTO teacher VALUES ('Bindu1', '@Bindu123');

CREATE TABLE reg_stud (
    username VARCHAR(20) NOT NULL,
    roll_no INT(20) UNSIGNED NOT NULL,
    address VARCHAR(50) NOT NULL,
    phno VARCHAR(11),
    password VARCHAR(20) NOT NULL,
    PRIMARY KEY (roll_no),
    UNIQUE (roll_no)
);

INSERT INTO reg_stud (username, roll_no, address, phno, password)
VALUES ('sampleuser', 10, 'samplecity', '8912345678', '123');

CREATE TABLE stud (
    roll_no INT(10) UNSIGNED NOT NULL,
    mark1 INT,
    mark2 INT,
    mark3 INT,
    mark4 INT,
    mark5 INT,
    mark6 INT,
    totalmarks INT,
    PRIMARY KEY (roll_no),
    UNIQUE (roll_no),
    FOREIGN KEY (roll_no)
        REFERENCES reg_stud(roll_no)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO stud
(roll_no, mark1, mark2, mark3, mark4, mark5, mark6, totalmarks)
VALUES
(10, 90, 13, 11, 44, 21, 67, 246);
