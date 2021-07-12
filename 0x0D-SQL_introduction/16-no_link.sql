-- Lists all records - MySQL server
-- Clause WHERE don't list rows without name value 
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
