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
    director_id_response = input("Director_ID to Select:  ")
    director_id = int(director_id_response)
    
    #validate input
    invalid_response = True
    while invalid_response:
        if director_id > 999 or director_id < 0:
            print('invalid input, try again')
            director_id_response = input("Director_ID to delete:  ")
            director_id = int(director_id_response)
        else: invalid_response = False
    
    #execute query
    data = (director_id_response,)
    query = "SELECT title, director_name FROM movieidswithdirectornames WHERE director_id = %s;"
    cursor = DataBase.cursor()
    cursor.execute(query,data)
    result = cursor.fetchall()
    for x in result:
        print(x)
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()