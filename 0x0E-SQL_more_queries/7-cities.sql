-- Creates a DB and table - On MySQL server
-- Statement for creates a DB called hbtn_0d_usa and table called states
-- Statement USE for open the DB to be used
-- Use of UNIQUE, AUTO_GENERATED, NOT NULL and PRIMARY KEY constraints
-- state_id must be a FK that references to id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES states (id),
name VARCHAR(256) NOT NULL);
