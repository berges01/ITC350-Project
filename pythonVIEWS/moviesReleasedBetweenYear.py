import mysql.connector
import datetime

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
    start_year_resp = input("Year Range Start (Input a Year):  ")
    start_year = int(start_year_resp)
    end_year_resp = input("Year Range End (Input a Year):  ")
    end_year = int(end_year_resp)
    
    #validate input
    present_date = datetime.date.today()
    year = int(present_date.year)
    invalid_response = True
    while invalid_response:
        if start_year < 0 or end_year > year:
            print('invalid input, try again')
            start_year_resp = input("Year Range Start (Input a Year):  ")
            start_year = int(start_year_resp)
            end_year_resp = input("Year Range End (Input a Year):  ")
            end_year = int(end_year_resp)
        else: invalid_response = False
    
    #execute query
    data = (start_year,end_year)
    query = "SELECT * FROM movie_mash.selectmovies WHERE Release_Year BETWEEN %s AND %s;"
    cursor = DataBase.cursor(prepared = True)
    cursor.execute(query,data)
    result = cursor.fetchall()
    for x in result:
        print(x)
    DataBase.commit()
    DataBase.close()


if __name__ == "__main__":
    main()
