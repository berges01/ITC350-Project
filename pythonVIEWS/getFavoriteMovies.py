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
    user_email_response = input("Enter user Email for thier favorite movies:  ")
    user_email = user_email_response
    5
    #validate input
    invalid_response = True
    while invalid_response:
        if len(user_email) > 40:
            print('invalid input, try again')
            user_email_response = input("Enter user Email for thier favorite movies:  ")
            user_email = user_email_response
        else: invalid_response = False
    
    #execute query
    data = (user_email,)
    query = "SELECT Title FROM movie_mash.favoritedmoviesformatted WHERE Email = %s;"
    cursor = DataBase.cursor(prepared = True)
    cursor.execute(query,data)
    result = cursor.fetchall()
    for x in result:
        print(x)
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()
