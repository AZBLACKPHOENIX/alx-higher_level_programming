-- Select cities.id, cities.name, and states.name from cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities, states
-- Filter records where cities.state_id matches states.id
WHERE cities.state_id = states.id
-- Sort results in ascending order by cities.id
ORDER BY cities.id ASC;
