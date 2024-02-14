-- Switch to the database hbtn_0d_2
USE hbtn_0d_2;

-- Create table unique_id if it doesn't already exist
CREATE TABLE IF NOT EXISTS unique_id (
    -- Define the id column as INT, NOT NULL, with a default value of 1, and it must be unique
    id INT NOT NULL DEFAULT 1 UNIQUE,
    -- Define the name column as VARCHAR(256)
    name VARCHAR(256)
);
