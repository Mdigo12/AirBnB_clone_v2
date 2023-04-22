-- Prepares a MySQL server for the project
-- A database hbnb_dev_db and a new user hbnb_dev (in localhost)
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;

-- USAGE
-- Run Script: cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
-- Test: echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db