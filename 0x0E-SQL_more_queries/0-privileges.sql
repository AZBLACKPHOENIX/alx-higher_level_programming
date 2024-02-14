-- Create user_0d_2 if it doesn't exist
CREATE USER 'user_0d_2'@'localhost';

-- Grant necessary privileges to user_0d_1
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'user_0d_1'@'localhost';

-- Grant necessary privileges to user_0d_2
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'user_0d_2'@'localhost';

-- Check privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
