import mysql.connector
import csv


def main():
    DataBase = CreateConnection()
    CreateCursor(DataBase)


def CreateConnection():
    DataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Viva La Vida2009!",
        database="movie_mash",
        port=3306
    )
    return DataBase


def CreateCursor(DataBase):
    with open('data/movie_data.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            try:
                print(" -------------- Movie -----------------")
                title = row['Title']
                print(title)
                release_year = row['Release_Date']
                print(release_year)
                imdb_rating = int(row['IMDB_Rating'])
                print(imdb_rating)
                movie_genre = row['Genre']
                print(movie_genre)
                content_rating = row['Content_Rating']
                print(content_rating)
                running_time = int(row['Running_Time'])
                print(running_time)
                movie_id = int(row['Movie_ID'])
                print(movie_id)
                imdb_link = row['IMDB_Link']
                print(imdb_link)
                director_id = row['Director_ID']
                print(director_id)
                values = (
                    title, release_year, imdb_rating, movie_genre, content_rating, running_time, movie_id, imdb_link,
                    director_id)
                query = 'INSERT INTO movie (Title, Release_Year, IMDB_Rating, Genre, Content_Rating, ' \
                        'Running_Time_Minutes, Movie_ID, IMDB_Link, Director_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, ' \
                        '%s, ' \
                        '%s)'
                cursor = DataBase.cursor()
                cursor.execute(query, values)
                DataBase.commit()
            except Exception as e:
                print("Error reading in CSV data or pushing to DB: %s" % e)
        DataBase.close()


if __name__ == "__main__":
    main()
