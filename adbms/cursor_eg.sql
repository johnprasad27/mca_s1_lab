DELIMITER //

CREATE PROCEDURE display_names()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE sname VARCHAR(50);

    DECLARE cur CURSOR FOR
        SELECT name FROM STUDENT;

    DECLARE CONTINUE HANDLER
    FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP

        FETCH cur INTO sname;

        IF done = 1 THEN
            LEAVE read_loop;
        END IF;

        SELECT sname;

    END LOOP;

    CLOSE cur;
END //

DELIMITER ;