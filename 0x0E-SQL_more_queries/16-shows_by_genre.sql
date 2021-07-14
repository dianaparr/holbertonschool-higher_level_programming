-- Lists all Comedy shows in the database hbtn_0d_tvshows - On MySQL server
-- Clause JOIN (RIGHT JOIN, returns all records from the right table (table2) that matched the ON condition)
-- table 1 = tv_show_genres & table 2 = tv_shows or tv_genres
SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC;
