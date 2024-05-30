-- Select genres and count the number of shows linked to each genre
SELECT genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;
