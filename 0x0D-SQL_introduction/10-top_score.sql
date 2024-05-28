-- Task 10: List all records of second_table ordered by score
-- This script lists all records of the table second_table from the database hbtn_0c_0,
-- displaying both score and name, and ordering the results by score in descending order.

SELECT score, name FROM second_table ORDER BY score DESC;
