-- Task 5: Print the full description of the table first_table
-- This script prints the full description of the table first_table from the database hbtn_0c_0.

SELECT TABLE_NAME, CREATE_TABLE 
FROM information_schema.tables 
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
