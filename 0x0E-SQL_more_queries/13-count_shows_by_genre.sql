-- Select genre and count the number of shows linked to each genre from tv_show_genres table
SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
-- Join tv_genres and tv_show_genres tables on genre_id
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Group by genre to count the number of shows linked to each genre
GROUP BY tv_genres.genre
-- Sort results in descending order by the number of shows linked
ORDER BY number_of_shows DESC;
