-- Select tv_shows.title and tv_show_genres.genre_id from tv_shows table
-- Left join tv_show_genres table to include shows that do not have a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Left join tv_show_genres on tv_shows.id equals tv_show_genres.show_id
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Filter out records where tv_show_genres.genre_id is not null (i.e., where a genre is linked)
WHERE tv_show_genres.genre_id IS NULL
-- Sort results in ascending order by tv_shows.title and tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
