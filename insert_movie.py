import mysql.connector
import csv

def main():
    DataBase = CreateConnection()
    CreateCursor(DataBase)

def CreateConnection():     
    DataBase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Viva La Vida2009!",
        database = "movie_mash_schema",
        port = 3306
    )
    return DataBase

def CreateCursor(DataBase):
    with open('./ITC350-Project/data/movie_data.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            print(" -------------- Movie -----------------")
            title = row['Title']
            print(title)
            release_date = row['Release_Date']
            print(release_date)
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
    values = (title,release_date,imdb_rating,movie_genre,content_rating,running_time,movie_id,imdb_link) 
    #values = ('test movie','11-11-2002',1,'test','PG',123,240,'test.com')      
    query = '''INSERT INTO movie_mash_schema.movie (Title, Release_Date, IMDB_Rating, Genre, Content_Rating, Running_Time, Movie_ID, IMDB_Link) VALUES (%s, %s, %d, %s, %s, %d, %d, %s )''' % values
    cursor = DataBase.cursor()
    cursor.execute(query)
    DataBase.commit()


if __name__ == "__main__":
    main()