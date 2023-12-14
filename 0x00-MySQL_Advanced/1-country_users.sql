--a SQL script that creates a table users
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- 
CREATE TABLE IF NOT EXISTS user(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL UNIQUE,
	email VARCHAR(255) NOT NULL UNIQUE,
	country CHAR(2) NOT NULL DEFAULT 'US'
        CHECK( country IN ('US', 'CO', 'TN'))
);	
