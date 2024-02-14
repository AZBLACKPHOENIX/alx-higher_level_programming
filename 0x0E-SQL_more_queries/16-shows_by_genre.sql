-- Select tv_shows.title and tv_genres.name
-- Join tv_genres and tv_show_genres tables on genre_id
-- Join tv_show_genres and tv_shows tables on show_id
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
-- Left join tv_show_genres and tv_shows on show_id
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
-- Left join tv_genres and tv_show_genres on genre_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
-- Sort results in ascending order by the show title and genre name
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
