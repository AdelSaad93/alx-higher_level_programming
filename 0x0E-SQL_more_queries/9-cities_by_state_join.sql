-- Task 9: Cities by States
-- This script lists all cities contained in the database hbtn_0d_usa with their respective states.

-- Use the database
USE hbtn_0d_usa;

-- Select cities along with their respective states
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
