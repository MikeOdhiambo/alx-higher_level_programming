-- Creates the table unique_id if it does not exist with attributes
-- id[INT] default value 1 and is unique, name[VARCHAR(256)]
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
