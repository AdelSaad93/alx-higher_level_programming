-- Task 3: Always a name
-- This script creates the table force_name on your MySQL server.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
