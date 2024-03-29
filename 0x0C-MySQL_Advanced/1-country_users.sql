-- script that creates a table 'users'
-- columns: id, email, name and country
CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255), country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL, PRIMARY KEY (id));