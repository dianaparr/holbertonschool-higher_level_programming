-- Creates DB and new user - On MySQL server
-- Statement which grants the permissions, in this case, to CREATE
-- privilege_level on user is only SELECT privilege in the DB created
-- Flow: create (DB), create (user), grant and reload
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2@localhost;
FLUSH PRIVILEGES;
