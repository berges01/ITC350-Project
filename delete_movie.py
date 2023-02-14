import mysql.connector
import csv


def main():
    DataBase = CreateConnection()
    CreateCursor(DataBase)


def CreateConnection():
    DataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="erik1999",
        database="movie_mash",
        port=3306
    )
    return DataBase


def CreateCursor(DataBase):
    with open('data/director_data.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        try:
            for row in reader:
                print(" -------------- Movie -----------------")
                movie_id = int(row['Movie_ID'])
                print(movie_id)
                try:
                    values = (Director_Name, Director_ID)
                    query = 'DELETE FROM movie_mash_schema (Movie_ID) VALUES (%s)'
                    cursor = DataBase.cursor()
                    cursor.execute(query, values)
                    DataBase.commit()
                    print(cursor.rowcount, "record inserted.")
                except Exception as insert_error:
                    print("DB Deletion Error: %s" % insert_error)
        except KeyError as e:
            print("Key Error (Key or Data Type Incorrect): %s" % e)
    DataBase.close()

if __name__ == "__main__":
    main()
