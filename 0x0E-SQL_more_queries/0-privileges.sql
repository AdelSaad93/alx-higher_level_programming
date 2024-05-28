-- Task 0: My privileges!
-- This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

-- Check if user_0d_1 exists and show grants if exists
SELECT 
    CASE
        WHEN EXISTS (SELECT 1 FROM mysql.user WHERE User = 'user_0d_1' AND Host = 'localhost')
        THEN SHOW GRANTS FOR 'user_0d_1'@'localhost'
        ELSE 'User user_0d_1 does not exist'
    END;

-- Check if user_0d_2 exists and show grants if exists
SELECT 
    CASE
        WHEN EXISTS (SELECT 1 FROM mysql.user WHERE User = 'user_0d_2' AND Host = 'localhost')
        THEN SHOW GRANTS FOR 'user_0d_2'@'localhost'
        ELSE 'User user_0d_2 does not exist'
    END;
