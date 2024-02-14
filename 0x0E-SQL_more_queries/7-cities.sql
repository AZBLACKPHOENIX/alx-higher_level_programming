-- Create database hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create table cities if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
    -- Define the id column as INT, unique, auto-generated, not null, and primary key
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    -- Define the state_id column as INT, not null, and foreign key referencing id column of states table
    state_id INT NOT NULL,
    -- Define the name column as VARCHAR(256), not null
    name VARCHAR(256) NOT NULL,
    -- Add foreign key constraint for state_id column
    FOREIGN KEY (state_id) REFERENCES states(id)
);
