# This script lists all records of the second_table in the hbtn_0c_0 database, excluding rows without a name value.
# Results display the score and the name in descending order of score.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
