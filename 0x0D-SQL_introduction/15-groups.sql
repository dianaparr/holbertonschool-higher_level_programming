-- Lists the number of records - MySQL server
-- Clause GROUP BY: to join rows that have the same scores
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
