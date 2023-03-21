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
    actor_response = input("Actor Name (Exact Match):  ")
    actor = str(actor_response)
    
    #validate input
    invalid_response = True
    while invalid_response:
        if len(actor) > 100:
            print('invalid input, response too long.')
            actor_response = input("Movie Genre (Exact Match):  ")
            actor = str(actor_response)
        else: invalid_response = False
    
    #execute query to check if genre exists.
    data = (actor,)
    query = "SELECT movie.Title FROM movie_mash.movieswithactor WHERE Actor_Name = %s GROUP BY Actor_Name;"
    cursor = DataBase.cursor(prepared = True)
    cursor.execute(query,data)
    result = cursor.fetchall()
    count = 0
    for x in result:
        count = count + 1
        print(x)
    if count == 0:
        print('No actor with this name was found. Check Spelling and Punctuation.')
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()
