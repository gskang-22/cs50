SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person.id = people.id
JOIN ratings ON ratings.movie_id = movies.id
ORDER BY ratings.rating DESC
LIMIT 5