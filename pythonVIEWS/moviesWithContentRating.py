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
    rating_response = input("Enter Rating (G,PG,PG-13,R) (Exact Match):  ")
    rating = str(rating_response)
    
    #validate input
    invalid_response = True
    while invalid_response:
        if len(rating) > 50 or rating not in ["G","PG","PG-13","R"]:
            print('invalid input, response too long or invalid. Try again.')
            rating_response = input("Enter Rating (G,PG,PG-13,R) (Exact Match):  ")
            rating = str(rating_response)
        else: invalid_response = False
    
    #execute query to check if genre exists.
    data = (rating,)
    query = "SELECT Title, Content_Rating FROM movie_mash.selectmovies WHERE Content_Rating = %s ORDER BY Title ASC;"
    cursor = DataBase.cursor()
    cursor.execute(query,data)
    result = cursor.fetchall()
    count = 0
    for x in result:
        count = count + 1
        print(x)
    if count == 0:
        print('No movies with a content rating of this type were found.')
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()
