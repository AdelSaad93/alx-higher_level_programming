-- Step 1: Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Step 2: Use the database
USE hbtn_0d_usa;

-- Step 3: Create the tables if they don't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Step 4: Insert data into the tables
INSERT INTO states (name) VALUES 
('California'), 
('Arizona'), 
('Texas'), 
('Nevada')
ON DUPLICATE KEY UPDATE name=name;

INSERT INTO cities (state_id, name) VALUES 
((SELECT id FROM states WHERE name='California'), 'San Francisco'), 
((SELECT id FROM states WHERE name='California'), 'San Diego'), 
((SELECT id FROM states WHERE name='California'), 'San Jose'), 
((SELECT id FROM states WHERE name='Arizona'), 'Page'), 
((SELECT id FROM states WHERE name='Arizona'), 'Phoenix'), 
((SELECT id FROM states WHERE name='Nevada'), 'Las Vegas')
ON DUPLICATE KEY UPDATE name=name;

-- Step 5: Query to list all cities of California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
