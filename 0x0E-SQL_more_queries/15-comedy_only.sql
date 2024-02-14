-- Select tv_shows.title from tv_shows table
-- Join tv_genres and tv_show_genres tables on genre_id
-- Join tv_show_genres and tv_shows tables on show_id
SELECT tv_shows.title
FROM tv_shows
-- Join tv_genres and tv_show_genres on genre_id
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Join tv_show_genres and tv_shows on show_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Filter records where the genre is Comedy
WHERE tv_genres.name = 'Comedy'
-- Sort results in ascending order by the show title
ORDER BY tv_shows.title ASC;
