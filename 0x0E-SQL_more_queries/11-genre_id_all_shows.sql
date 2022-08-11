-- Lists all shows contained in the db hbtn_0d_tvshows in the as tv_shows.title - tv_show_genres.genre_id
-- sorted un ascending order by tv_shows.title and tv_show_genres.genre_id
-- displays null if a show doesn't have a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

