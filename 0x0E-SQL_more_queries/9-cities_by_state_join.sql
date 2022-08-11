-- Lists all cities contained in the db hbtn_0d_usa
-- Each record displays cities.id - cities.name - states.name in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id;
