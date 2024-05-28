-- Task 12: Update Bob's score to 10
-- This script updates the score of Bob to 10 in the table second_table from the database hbtn_0c_0.
-- It only uses the name field and not the id value.

UPDATE second_table SET score = 10 WHERE name = 'Bob';
