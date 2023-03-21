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

#stolen from selectMovie.py
def CreateCursor(DataBase):
    #grab input
    actor_id_response = input("Actor ID to Select:  ")
    actor_id = int(actor_id_response)
    
    #validate input
    invalid_response = True
    while invalid_response:
        if actor_id > 9999 or actor_id < 0: #POTENTIALBUG: select count?
            print('invalid input, try again')
            actor_id_response = input("Actor_ID to delete:  ")
            actor_id = int(actor_id_response)
        else: invalid_response = False
    
    #execute query
    data = (actor_id_response,)
    query = "SELECT actor_id, actor_name, award_name FROM actornameswithawardnames WHERE actor_id = %s;"
    cursor = DataBase.cursor()
    cursor.execute(query,data)
    result = cursor.fetchall()
    for x in result:
        print(x)
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()