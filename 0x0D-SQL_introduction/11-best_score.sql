-- Lists all records of the table - MySQL server
-- The statements should display both the score (ordered, top first and where score >= 10) and the name
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
