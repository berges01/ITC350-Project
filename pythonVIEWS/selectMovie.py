import mysql.connector
from dotenv import load_dotenv
import os

def main():
    DataBase = CreateConnection()
    CreateCursor(DataBase)


def CreateConnection():
    DataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get("passwd"),
        database="movie_mash",
        port=3306
    )
    return DataBase


def CreateCursor(DataBase):
    #grab input
    movie_id_response = input("Movie ID to Select:  ")
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
    data = (movie_id,)
    query = "SELECT * FROM movie_mash.selectmovies WHERE movie_id = %s;"
    cursor = DataBase.cursor(prepared = True)
    cursor.execute(query,data)
    result = cursor.fetchall()
    for x in result:
        print(x)
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()
