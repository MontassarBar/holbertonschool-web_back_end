--script that creates a stored procedure AddBonus that adds a new correction for a student
--columns:
DELIMITER //
CREATE Procedure AddBonusss (IN user_id int, IN project_name VARCHAR(255), IN score int)
BEGIN
IF EXISTS (SELECT * FROM projects WHERE project.name = project_name) = 0 THEN
INSERT INTO projects (name) VALUES (project_name);
END IF;
INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = projects_name), score);
END;//
DELIMITER ;