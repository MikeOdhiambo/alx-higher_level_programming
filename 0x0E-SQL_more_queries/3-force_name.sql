-- Creates the table force_name with attributes id [INT], name [VARCHAR(256)] if it doesn't exist 
-- name cannot be NULL
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
