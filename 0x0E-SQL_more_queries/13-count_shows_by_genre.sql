-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Displays <TV Show genre> - <Number of shows linked to this genre> with first column as 'genre'
-- second column as 'number_of_shows' sorted in ascending order by number of shows
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
