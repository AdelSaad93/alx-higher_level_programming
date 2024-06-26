-- Select shows with at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_shows.title, tv_show_genres.genre_id
HAVING COUNT(tv_show_genres.genre_id) >= 1
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
