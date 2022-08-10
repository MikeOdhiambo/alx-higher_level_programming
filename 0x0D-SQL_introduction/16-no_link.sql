-- Lists all records of the table second_table except rows without a name value
-- Results display the score and name respectively and in descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
