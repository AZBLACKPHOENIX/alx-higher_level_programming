SELECT city, AVG(temperature) AS average_temperature_Fahrenheit
FROM temperatures
GROUP BY city
ORDER BY average_temperature_Fahrenheit DESC;
