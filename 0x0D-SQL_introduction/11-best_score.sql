-- Task 11: List records with score >= 10
-- This script lists all records with a score >= 10 from the table second_table in the database hbtn_0c_0.
-- It displays both the score and the name, ordered by score in descending order.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
