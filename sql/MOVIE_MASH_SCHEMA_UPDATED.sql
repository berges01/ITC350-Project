CREATE TABLE Users
(
  FirstName CHAR(30) NOT NULL,
  LastName CHAR(30) NOT NULL,
  UserID INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (UserID)
);

CREATE TABLE Director
(
  Director_Name CHAR(50) NOT NULL,
  Director_ID INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Director_ID)
);

CREATE TABLE Actors
(
  Actor_Name CHAR(50) NOT NULL,
  Actor_ID INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Actor_ID)
);

CREATE TABLE Award
(
  Award_Name CHAR(50) NOT NULL,
  Award_ID INT NOT NULL AUTO_INCREMENT,
  Year_Awarded INT(4) NOT NULL,
  PRIMARY KEY (Award_ID)
);

CREATE TABLE Movie
(
  Title CHAR(50) NOT NULL,
  Release_Year INT(4) NOT NULL,
  IMDB_Rating_Percentage INT(3) NOT NULL,
  Genre CHAR(30) NOT NULL,
  Content_Rating CHAR(8) NOT NULL,
  Running_Time_Minutes INT(3) NOT NULL,
  Movie_ID INT NOT NULL AUTO_INCREMENT,
  IMDB_Link TEXT(500) NOT NULL,
  Director_ID INT NOT NULL,
  PRIMARY KEY (Movie_ID),
  FOREIGN KEY (Director_ID) REFERENCES Director(Director_ID)
);

CREATE TABLE FavoritedByFavorite
(
  Movie_ID INT NOT NULL,
  UserID INT NOT NULL,
  PRIMARY KEY (Movie_ID, UserID),
  FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE HasActor
(
  Movie_ID INT NOT NULL,
  Actor_ID INT NOT NULL,
  PRIMARY KEY (Movie_ID, Actor_ID),
  FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID),
  FOREIGN KEY (Actor_ID) REFERENCES Actors(Actor_ID)
);

CREATE TABLE HasAward
(
  Award_ID INT NOT NULL,
  Movie_ID INT NOT NULL,
  PRIMARY KEY (Award_ID, Movie_ID),
  FOREIGN KEY (Award_ID) REFERENCES Award(Award_ID),
  FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID)
);