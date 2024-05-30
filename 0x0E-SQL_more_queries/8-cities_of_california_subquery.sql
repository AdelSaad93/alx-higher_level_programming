-- Task 8: Cities of California
-- This script lists all cities of California from the database hbtn_0d_usa.

-- Use the database
USE hbtn_0d_usa;

-- Select cities from California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
