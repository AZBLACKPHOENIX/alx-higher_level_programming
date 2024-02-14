-- Switch to the database hbtn_0d_2
USE hbtn_0d_2;

-- Create table id_not_null if it doesn't already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    -- Define the id column as INT, NOT NULL, with a default value of 1
    id INT NOT NULL DEFAULT 1,
    -- Define the name column as VARCHAR(256)
    name VARCHAR(256)
);
