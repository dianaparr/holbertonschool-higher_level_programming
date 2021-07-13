-- Lists all the cities of California - On MySQL server
-- Subquery to list the California cities (state_id=1) found in that DB (hbtn_0d_usa)
SELECT id, name
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id DESC;
