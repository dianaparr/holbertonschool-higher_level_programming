-- Create a table and create some records - MySQL server
-- Command for create a new table called second_table, and statements for insert information in each row
CREATE TABLE IF NOT EXISTS second_table (id INT,
name VARCHAR(256),
score INT);
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
