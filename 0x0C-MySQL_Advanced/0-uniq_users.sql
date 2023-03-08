-- script that creates a table 'users'
-- columns: id, email and name
CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255), PRIMARY KEY (id));
