import mysql.connector
import csv


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
    with open('data/hasAward_data.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        try:
            for row in reader:
                print(" -------------- Actor -----------------")
                Movie_ID = row['Movie_ID']
                print(Movie_ID)
                Award_ID = row['Award_ID']
                print(Award_ID)
                try:
                    values = (Movie_ID, Award_ID)
                    query = 'INSERT INTO hasaward (Movie_ID, Award_ID) VALUES (%s, %s)'
                    cursor = DataBase.cursor()
                    cursor.execute(query, values)
                    DataBase.commit()
                    print(cursor.rowcount, "record inserted.")
                except Exception as insert_error:
                    print("DB Insertion Error: %s" % insert_error)
        except KeyError as e:
            print("Key Error (Key or Data Type Incorrect): %s" % e)
    DataBase.close()


if __name__ == "__main__":
    main()
