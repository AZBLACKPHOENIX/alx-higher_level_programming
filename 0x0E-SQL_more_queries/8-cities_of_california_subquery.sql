-- Select all cities where state_id corresponds to California's id
SELECT * 
FROM cities
WHERE state_id = (
    -- Subquery to get the id of California from states table
    SELECT id 
    FROM states 
    WHERE name = 'California'
)
ORDER BY id ASC; -- Sorting results in ascending order by cities.id
