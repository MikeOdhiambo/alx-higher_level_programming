-- Lists the number of records with the same score in the table second_table
-- Result displays the score and number of records for this score with label 'number'
--- List is sorted by number of records (DESC)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
