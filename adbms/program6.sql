CREATE DATABASE stores;
USE stores;

CREATE TABLE Product(
    PdtId INT PRIMARY KEY,
    Pname VARCHAR(20),
    Price DOUBLE,
    Qtyinstock INT
);

CREATE TABLE Sale(
    saleId INT PRIMARY KEY,
    Deliveryaddress VARCHAR(50)
);

CREATE TABLE Saleitem(
    saleId INT,
    PdtId INT,
    Qty INT,
    PRIMARY KEY(saleId,PdtId),
    FOREIGN KEY(saleId) REFERENCES Sale(saleId),
    FOREIGN KEY(PdtId) REFERENCES Product(PdtId)
);

DELIMITER //

CREATE TRIGGER updateQty
AFTER INSERT ON Saleitem
FOR EACH ROW
BEGIN
UPDATE Product
SET Qtyinstock = Qtyinstock - NEW.Qty
WHERE PdtId = NEW.PdtId;
END //

DELIMITER ;