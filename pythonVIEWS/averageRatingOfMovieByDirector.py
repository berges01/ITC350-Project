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
    director_response = input("Director Name (Exact Match):  ")
    director = str(director_response)
    
    #validate input
    invalid_response = True
    while invalid_response:
        if len(director) > 100:
            print('invalid input, response too long.')
            director_response = input("Director Name (Exact Match):  ")
            director = str(director_response)
        else: invalid_response = False
    
    #execute query to check if genre exists.
    data = (director,)
    query = "SELECT Director_Name, AVG(IMDB_Rating) FROM movie_mash.averageratingofmoviebydirector WHERE Director_Name = %s GROUP BY Director_Name;"
    cursor = DataBase.cursor(prepared = True)
    cursor.execute(query,data)
    result = cursor.fetchall()
    count = 0
    for x in result:
        count = count + 1
        print(x)
    if count == 0:
        print('No director with this name was found. Check Spelling and Punctuation.')
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()
