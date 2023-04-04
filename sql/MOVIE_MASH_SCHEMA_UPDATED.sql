CREATE TABLE users
(
  FirstName CHAR(30) NOT NULL,
  LastName CHAR(30) NOT NULL,
  Email CHAR(40),
  Passwd CHAR(200) NOT NULL,
  PRIMARY KEY (Email)
);

CREATE TABLE director
(
  Director_Name CHAR(50) NOT NULL,
  Director_ID INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Director_ID)
);

CREATE TABLE actors
(
  Actor_Name CHAR(50) NOT NULL,
  Actor_ID INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Actor_ID)
);

CREATE TABLE award
(
  Award_Name CHAR(50) NOT NULL,
  Award_ID INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Award_ID)
);

CREATE TABLE movie
(
  Title CHAR(50) NOT NULL,
  Release_Year INT(4) NOT NULL,
  IMDB_Rating INT(3) NOT NULL,
  Genre CHAR(30) NOT NULL,
  Content_Rating CHAR(8) NOT NULL,
  Running_Time_Minutes INT(3) NOT NULL,
  Movie_ID INT NOT NULL AUTO_INCREMENT,
  IMDB_Link TEXT(500) NOT NULL,
  Director_ID INT NOT NULL,
  PRIMARY KEY (Movie_ID),
  FOREIGN KEY (Director_ID) REFERENCES director(Director_ID)
);

CREATE TABLE favoritedbyfavorite
(
  Movie_ID INT NOT NULL,
  Email CHAR(40) NOT NULL,
  PRIMARY KEY (Movie_ID, Email),
  FOREIGN KEY (Movie_ID) REFERENCES movie(Movie_ID),
  FOREIGN KEY (Email) REFERENCES users(Email)
);

CREATE TABLE hasactor
(
  Movie_ID INT NOT NULL,
  Actor_ID INT NOT NULL,
  PRIMARY KEY (Movie_ID, Actor_ID),
  FOREIGN KEY (Movie_ID) REFERENCES movie(Movie_ID),
  FOREIGN KEY (Actor_ID) REFERENCES actors(Actor_ID)
);

CREATE TABLE hasaward
(
  Award_ID INT NOT NULL,
  Movie_ID INT NOT NULL,
  PRIMARY KEY (Award_ID, Movie_ID),
  FOREIGN KEY (Award_ID) REFERENCES award(Award_ID),
  FOREIGN KEY (Movie_ID) REFERENCES movie(Movie_ID)
);