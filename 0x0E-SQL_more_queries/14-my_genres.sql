-- Select tv_genres.name from tv_genres table
-- Join tv_genres and tv_show_genres tables on genre_id
-- Join tv_show_genres and tv_shows tables on show_id
SELECT tv_genres.name
FROM tv_genres
-- Join tv_genres and tv_show_genres on genre_id
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Join tv_show_genres and tv_shows on show_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Filter records where the title is Dexter
WHERE tv_shows.title = 'Dexter'
-- Sort results in ascending order by genre name
ORDER BY tv_genres.name ASC;

