-- Task 4: ID can't be null
-- This script creates the table id_not_null on your MySQL server.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1 NOT NULL,
    name VARCHAR(256)
);
