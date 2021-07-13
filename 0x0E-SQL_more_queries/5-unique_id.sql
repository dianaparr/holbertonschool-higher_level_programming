-- Creates a table - On MySQL server
-- Statement for creates a table called unique_id in the current database
-- Use of DEFAULT and UNIQUE constraints
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
