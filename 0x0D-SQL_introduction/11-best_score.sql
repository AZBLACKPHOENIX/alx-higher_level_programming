--This script selects and lists all records with a score greater than or equal to 10 from the second_table in the hbtn_0c_0 database.--It displays both the score and the name, ordered by score in descending order.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
