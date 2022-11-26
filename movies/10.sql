SELECT DISTINCT name FROM people
JOIN stars ON stars.person_id = people.id
JOIN movies ON movies.id = stars.movie_id
JOIN ratings ON rating.movie_id = movies.id
WHERE ratings.rating >= 9.0;