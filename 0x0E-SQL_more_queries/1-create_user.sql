-- Creates the MySQL user user_0d_1 with all privileges if they don't already exist
-- Sets the password to user_0d_1_pwd
CREATE USER IF NOT ALREADY EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
