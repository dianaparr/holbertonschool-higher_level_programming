-- Creates the MySQL server user - On MySQL server
-- Statement which grants the permissions, in this case, to CREATE
-- Flow: create, grant and reload
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL
ON *.*
TO user_0d_1@localhost;
FLUSH PRIVILEGES;
