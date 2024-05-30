-- Select genres and count the number of shows linked to each genre
SELECT genres.name AS genre, COUNT(shows.id) AS number_of_shows
FROM genres
LEFT JOIN shows ON genres.id = shows.genre_id
GROUP BY genres.id
ORDER BY number_of_shows DESC;
