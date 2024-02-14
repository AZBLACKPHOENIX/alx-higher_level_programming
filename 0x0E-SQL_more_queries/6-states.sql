-- Create database hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create table states if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    -- Define the id column as INT, unique, auto-generated, not null, and primary key
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    -- Define the name column as VARCHAR(256), not null
    name VARCHAR(256) NOT NULL
);
