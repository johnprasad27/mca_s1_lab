CREATE DATABASE store;
USE store;

CREATE TABLE Product(
    PdtId INT PRIMARY KEY,
    PName VARCHAR(20),
    Price DOUBLE,
    Quantity INT
);

DELIMITER //

CREATE PROCEDURE Insertproduct(IN id INT, IN name VARCHAR(20), IN price DOUBLE, IN qty INT)
BEGIN
IF price>0 AND qty>=0 THEN
INSERT INTO Product VALUES(id,name,price,qty);
END IF;
END //

DELIMITER ;

CALL Insertproduct(1001,'Pen',10,5);