-- Ensure the database exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Ensure the states table exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Ensure the cities table exists
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Insert sample data into the states table
INSERT INTO states (id, name) VALUES 
(1, 'California'), 
(2, 'Arizona'), 
(3, 'Texas'), 
(4, 'Nevada')
ON DUPLICATE KEY UPDATE id=id;

-- Insert sample data into the cities table
INSERT INTO cities (id, state_id, name) VALUES 
(1, 1, 'San Francisco'), 
(2, 1, 'San Diego'), 
(3, 1, 'San Jose'), 
(10, 2, 'Page'), 
(11, 2, 'Phoenix'), 
(12, 4, 'Las Vegas') 
ON DUPLICATE KEY UPDATE id=id;

-- Query to list all cities along with their respective states
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
