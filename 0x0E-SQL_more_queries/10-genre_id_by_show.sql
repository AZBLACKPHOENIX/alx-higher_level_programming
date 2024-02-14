-- Select tv_shows.title and tv_show_genres.genre_id from tv_shows and tv_show_genres tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Join tv_shows and tv_show_genres tables on tv_shows.id equals tv_show_genres.show_id
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Ensure that there is at least one genre linked for each show
WHERE tv_shows.id IN (SELECT DISTINCT show_id FROM tv_show_genres)
-- Sort results in ascending order by tv_shows.title and tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
