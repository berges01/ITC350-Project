from dotenv import load_dotenv
load_dotenv()

import mysql.connector
import os

def main():
    DataBase = CreateConnection()
    CreateCursor(DataBase)


def CreateConnection():
    DataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get('passwd'),
        database="movie_mash",
        port=3306
    )
    return DataBase


def CreateCursor(DataBase):
    #grab input
    movie_id_response = input("Movie_ID to delete:  ")
    movie_id = int(movie_id_response)
    
    #validate input
    invalid_response = True
    while invalid_response:
        if movie_id > 9999 or movie_id < 0:
            print('invalid input, try again')
            movie_id_response = input("Movie_ID to delete:  ")
            movie_id = int(movie_id_response)
        else: invalid_response = False
    
    #execute query
    query = "DELETE FROM movie_mash.movies WHERE movie_id= '" + movie_id_response + "';"
    cursor = DataBase.cursor()
    cursor.execute(query)
    DataBase.commit()
    print(cursor.rowcount, "record deleted.")
    DataBase.close()


if __name__ == "__main__":
    main()
