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
    #grab input
    genre_response = input("Movie Genre (Exact Match):  ")
    genre = str(genre_response)
    
    #validate input
    invalid_response = True
    while invalid_response:
        if len(genre) > 50:
            print('invalid input, response too long.')
            genre_response = input("Movie Genre (Exact Match):  ")
            genre = str(genre_response)
        else: invalid_response = False
    
    #execute query to check if genre exists.
    data = (genre,)
    query = "SELECT * FROM movie_mash.selectmovies WHERE Genre = %s ORDER BY Genre ASC;"
    cursor = DataBase.cursor()
    cursor.execute(query,data)
    result = cursor.fetchall()
    count = 0
    for x in result:
        count = count + 1
        print(x)
    if count == 0:
        print('No genre of this type was found.')
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()
