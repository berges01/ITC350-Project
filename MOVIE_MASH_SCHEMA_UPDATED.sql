CREATE TABLE Users
(
  FirstName CHAR(20) NOT NULL,
  UserName CHAR(20) NOT NULL,
  LastName CHAR(20) NOT NULL,
  PRIMARY KEY (UserName)
);

CREATE TABLE Director
(
  Director_Name CHAR(40) NOT NULL,
  Director_ID INT NOT NULL,
  PRIMARY KEY (Director_ID)
);

CREATE TABLE Actors
(
  Actor_Name CHAR(40) NOT NULL,
  Actor_ID INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Actor_ID)
);

CREATE TABLE Award
(
  Award_Name CHAR(50) NOT NULL,
  Award_ID INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Award_ID)
);

CREATE TABLE Movie
(
  Title TEXT(50) NOT NULL,
  Release_Date DATE NOT NULL,
  IMDB_Rating INT NOT NULL,
  Genre CHAR(20) NOT NULL,
  Content_Rating CHAR(8) NOT NULL,
  Running_Time INT NOT NULL,
  Movie_ID INT NOT NULL AUTO_INCREMENT,
  IMDB_Link TEXT NOT NULL,
  Director_ID INT NOT NULL,
  PRIMARY KEY (Movie_ID),
  FOREIGN KEY (Director_ID) REFERENCES Director(Director_ID)
);

CREATE TABLE FavoritedByFavorite
(
  Movie_ID INT NOT NULL,
  UserName INT NOT NULL,
  PRIMARY KEY (Movie_ID, UserName),
  FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID),
  FOREIGN KEY (UserName) REFERENCES Users(UserName)
);

CREATE TABLE HasActors
(
  Movie_ID INT NOT NULL,
  Actor_ID INT NOT NULL,
  PRIMARY KEY (Movie_ID, Actor_ID),
  FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID),
  FOREIGN KEY (Actor_ID) REFERENCES Actors(Actor_ID)
);

CREATE TABLE hasAwards
(
  Award_ID INT NOT NULL,
  Movie_ID INT NOT NULL,
  PRIMARY KEY (Award_ID, Movie_ID),
  FOREIGN KEY (Award_ID) REFERENCES Award(Award_ID),
  FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID)
);

CREATE TABLE MovieFavoritedByUser
(
  Favorited_By_Username INT NOT NULL,
  Movie_ID INT NOT NULL,
  PRIMARY KEY (Favorited_By_Username, Movie_ID),
  FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID)
);