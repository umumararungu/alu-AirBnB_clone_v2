<<<<<<< HEAD
-- A script for MySQL serve test file for the project 

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES
=======
-- Create test database and user
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test' @'localhost';
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test' @'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
