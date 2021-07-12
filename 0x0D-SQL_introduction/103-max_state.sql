-- Import in database an table (mysql -u username -p  databasename  < path/example.sql)
-- Displays the max temperature of each state (ordered by State name)
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state DESC;
