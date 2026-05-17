DELIMITER //

CREATE PROCEDURE even_odd(IN num INT)
BEGIN
IF num%2=0 THEN
SELECT 'Even';
ELSE
SELECT 'Odd';
END IF;
END //

DELIMITER ;

CALL even_odd(8);
------------------------------------

DELIMITER //

CREATE PROCEDURE `grade`(in g int) 
BEGIN 
 declare des varchar(50); 
 if g > 90 
 then 
 set des="Grade is A"; 
 elseif g > 80 
 then 
 set des="Grade is B"; 
 elseif g > 70 
 then 
 set des="Grade is C"; 
 elseif g > 60 
 then 
 set des="Grade is D"; 
     else 
        set des="Grade is E"; 
    end if; 
    select g as Marks,des as Grade; 
END 

DELIMITER ;

_____________________________________________________


DELIMITER //

CREATE PROCEDURE grade(IN g INT)
BEGIN
    DECLARE des VARCHAR(50);

    IF g > 90 THEN
        SET des = 'Grade is A';

    ELSEIF g > 80 THEN
        SET des = 'Grade is B';

    ELSEIF g > 70 THEN
        SET des = 'Grade is C';

    ELSEIF g > 60 THEN
        SET des = 'Grade is D';

    ELSE
        SET des = 'Grade is E';

    END IF;

    SELECT g AS Marks, des AS Grade;
END //

DELIMITER ;

______________________________________________________


DELIMITER //

CREATE PROCEDURE `pos_neg_zero`(IN num INT)
BEGIN
    DECLARE r VARCHAR(10);

    IF num > 0 THEN
        SET r = 'positive';

    ELSEIF num < 0 THEN
        SET r = 'negative';

    ELSE
        SET r = 'zero';

    END IF;

    SELECT num AS Number, r AS Result;
END //

DELIMITER ;

_____________________________________________________
DELIMITER //

CREATE PROCEDURE `day_proc`(IN d DATE)
BEGIN
    DECLARE dat VARCHAR(10);

    SET dat = DAYNAME(d);

    SELECT d AS Date, dat AS WeekDay;
END //

DELIMITER ;

CALL day_proc('2025-05-18');

__________________________________________________________________

DELIMITER //

CREATE PROCEDURE `fact`(IN num INT)
BEGIN
    DECLARE f INT DEFAULT 1;
    DECLARE n1 INT;

    SET n1 = num;

    WHILE num > 0 DO
        SET f = f * num;
        SET num = num - 1;
    END WHILE;

    SELECT n1 AS Number, f AS Factorial;
END //

DELIMITER ;

CALL fact(5);