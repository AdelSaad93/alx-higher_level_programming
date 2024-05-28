-- Task 0: My privileges!
-- This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

-- Create user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Create user_0d_2 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
