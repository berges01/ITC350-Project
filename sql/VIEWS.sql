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

CREATE VIEW 'selectmovies' AS
SELECT *
FROM movie
ORDER BY Title ASC;

CREATE VIEW `uniquegenre` AS
SELECT distinct Genre
FROM movie
ORDER BY Genre ASC;

CREATE VIEW `averageratingofmoviewithactor` AS
SELECT actors.Actor_Name, actors.Actor_ID, hasactor.Movie_ID, movie.IMDB_Rating
FROM actors
INNER JOIN hasactor ON actors.Actor_ID = hasactor.Actor_ID
INNER JOIN movie ON hasactor.Movie_ID = movie.Movie_ID;

CREATE VIEW `favoritedmoviesformatted` AS
SELECT movie.Title, favoritedbyfavorite.UserID, users.FirstName, users.LastName
FROM users
INNER JOIN favoritedbyfavorite ON users.UserID = favoritedbyfavorite.UserID
INNER JOIN movie ON favoritedbyfavorite.Movie_ID = movie.Movie_ID;









/*movie ID <-> actor name - USED FOR actorswithawards AND actorswithdirectors*/
CREATE VIEW `movieidswithactornames` AS
SELECT hasActor.movie_id, hasActor.actor_id, actors.actor_name 
FROM hasActor 
INNER JOIN actor ON
actor.id=hasActor.actor_id;

/*getting movieIDs with award names*/
CREATE VIEW `movieidswithawardnames` AS SELECT hasAward.movie_id, hasAward.award_id, award.award_name
FROM hasAward
INNER JOIN award ON
award.award_id=hasAward.award_id
ORDER BY movie_id ASC;

/*actor <-> award*/
CREATE VIEW `actornameswithawardnames` AS
SELECT movieidswithactornames.actor_id, movieidswithactornames.actor_name, movieidswithawardnames.award_name, movieidswithawardnames.award_id
FROM movieidswithactornames 
INNER JOIN movieidswithawardnames ON 
movieidswithawardnames.movie_id=movieidswithactornames.movie_id
ORDER BY actor_id ASC;

/*movie_id <-> director_id*/
CREATE VIEW `movieidswithdirectornames` AS SELECT movie.movie_id, movie.director_id, director.director_name
FROM movie
INNER JOIN director ON
movie.director_id = director.director_id
ORDER BY director_id ASC;

/* actor <-> director VIA movie_id*/
CREATE VIEW `actornameswithdirectornames` AS SELECT movieidswithdirectornames.movie_id, movieidswithdirectornames.director_name, movieidswithdirectornames.director_id, movieidswithactornames.actor_name, movieidswithactornames.actor_id
FROM movieidswithactornames
INNER JOIN movieidswithdirectornames ON
movieidswithdirectornames.movie_id=movieidswithactornames.movie_id
ORDER BY movie_id ASC;