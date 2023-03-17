import mysql.connector


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
    query = "SELECT * FROM movie_mash.sortbyrating"
    cursor = DataBase.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
