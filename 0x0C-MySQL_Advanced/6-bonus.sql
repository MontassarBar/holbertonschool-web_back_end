--script that creates a stored procedure AddBonus that adds a new correction for a student
--columns:
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE Procedure AddBonus (IN user_id int, IN project_name VARCHAR(255), IN score int)
BEGIN
IF EXISTS (SELECT * FROM projects WHERE projects.name = project_name) = 0 THEN
INSERT INTO projects (name) VALUES (project_name);
END IF;
INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;//
DELIMITER ;

~                                   