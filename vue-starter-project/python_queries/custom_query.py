from flask import Flask, jsonify
import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')

def main():
    user_query = input("Enter Query: ")
    DataBase = CreateConnection()
    CreateCursor(DataBase,user_query)


def CreateConnection():
    DataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get("passwd"),
        database="movie_mash",
        port=3306
    )
    return DataBase


def CreateCursor(DataBase,user_query):
    query = user_query
    cursor = DataBase.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print(r)

if __name__ == "__main__":
    main()