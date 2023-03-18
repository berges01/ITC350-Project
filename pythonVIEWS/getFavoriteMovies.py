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
    user_id_response = input("Enter UserID for thier favorite movies:  ")
    user_id = int(user_id_response)
    5
    #validate input
    invalid_response = True
    while invalid_response:
        if user_id < 0:
            print('invalid input, try again')
            user_id_response = input("Movie ID to Select:  ")
            user_id = int(user_id_response)
        else: invalid_response = False
    
    #execute query
    data = (user_id,)
    query = "SELECT Title FROM movie_mash.favoritedmoviesformatted WHERE UserID = %s;"
    cursor = DataBase.cursor(prepared = True)
    cursor.execute(query,data)
    result = cursor.fetchall()
    for x in result:
        print(x)
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()
