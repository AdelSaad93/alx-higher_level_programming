-- Task 16: List all records with a name in second_table
-- This script lists all records of the table second_table from the database hbtn_0c_0.
-- It filters out rows without a name value and displays the score and name in descending order of score.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
