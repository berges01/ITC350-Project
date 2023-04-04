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
    query = "SELECT * FROM movie ORDER BY Title ASC"
    cursor = DataBase.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
