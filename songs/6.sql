SELECT name FROM songs
where artist_id = (SELECT id FROM artist WHERE name = "Post Malone");