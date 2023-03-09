-- script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0
-- The function SafeDiv takes 2 arguments: a and b
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
IF b = 0 THEN
RETURN 0;
END IF;
END//
RETURN a / b
DELIMITER ;