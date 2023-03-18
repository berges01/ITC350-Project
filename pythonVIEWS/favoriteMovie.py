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
    try:    
        print(" -------------- Favorite Movie------------- ")
        movie_id_response = input("Movie ID to favorite:  ")
        movie_id = int(movie_id_response)
        user_id_response = input("User ID: ")
        user_id = int(user_id_response)   
    
        invalid_response = True
        while invalid_response:
            if user_id < 0 or movie_id < 0:
                movie_id_response = input("Movie ID to favorite:  ")
                movie_id = int(movie_id_response)
                user_id_response = input("User ID: ")
                user_id = int(user_id_response)   
            else: invalid_response = False 
        try:

            values = (movie_id, user_id)
            query = 'INSERT INTO favoritedbyfavorite (Movie_ID, UserID) VALUES (%s, %s)'
            cursor = DataBase.cursor(prepared = True)
            cursor.execute(query, values)
            DataBase.commit()
            print(cursor.rowcount, "record inserted.")
        except Exception as insert_error:
            print("DB Insertion Error: %s" % insert_error)
    except KeyError as e:
            print("Key Error (Key or Data Type Incorrect): %s" % e)
    DataBase.close()


if __name__ == "__main__":
    main()
