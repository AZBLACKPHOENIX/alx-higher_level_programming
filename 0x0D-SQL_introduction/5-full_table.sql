#show full description of a table
SELECT TABLE_NAME
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
