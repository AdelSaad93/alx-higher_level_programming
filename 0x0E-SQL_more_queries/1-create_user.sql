-- Task 1: Root user
-- This script creates the MySQL server user user_0d_1.

-- Create user user_0d_1 if it doesn't exist and grant all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
