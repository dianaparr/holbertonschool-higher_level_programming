-- Lists all shows contained in hbtn_0d_tvshows - On MySQL server
-- Clause JOIN (LEFT JOIN, returns all records from the tv_shows table (table1) that matched the ON condition.)
-- table one: tv_shows and table two: tv_show_genres
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
