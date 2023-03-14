CREATE VIEW `highlyratedmovies` AS
SELECT Title,IMDB_Rating
FROM movie
WHERE IMDB_Rating >= 8
ORDER BY IMDB_Rating DESC;

CREATE VIEW `moviesbyreleasedate` AS
SELECT Title,Release_Year
FROM movie
ORDER BY Release_Year DESC;

CREATE VIEW `moviesbyruntime` AS
SELECT Title,Running_Time_Minutes
FROM movie
ORDER BY Running_Time_Minutes DESC;

CREATE VIEW `moviesundertwohours` AS
SELECT Title,Running_Time_Minutes
FROM movie
WHERE Running_Time_Minutes <= 120;

CREATE VIEW `moviessortedbytitle` AS
SELECT *
FROM movie
ORDER BY Title ASC;


CREATE VIEW `moviesbydirectorname` AS
SELECT movie.Title, director.Director_Name
FROM movie
INNER JOIN director ON
movie.Director_ID=director.Director_ID
ORDER BY director.Director_Name ASC;

CREATE VIEW `sortbyrating` AS
SELECT Title, IMDB_Rating
FROM movie
ORDER BY IMDB_Rating DESC;

CREATE VIEW `sortbygenre` AS
SELECT Title,Genre
FROM Movie
ORDER BY Genre ASC;