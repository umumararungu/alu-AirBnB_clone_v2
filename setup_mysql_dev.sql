<<<<<<< HEAD
-- A Script that prepares a MySQL serve for the project 

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
=======
-- Create dev database and user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev' @'localhost';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev' @'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
