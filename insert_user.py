import mysql.connector
import csv

def main():
    DataBase = CreateConnection()
    CreateCursor(DataBase)

def CreateConnection():
    DataBase = mysql.connector.connect(
        host = "localhost",
        user="root",
        passwd="Viva La Vida2009!",
        database="movie_mash",
        port=3306
    )
    return DataBase


def CreateCursor(DataBase):
    with open('data/user_data.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        try:
            for row in reader:
                FirstName = row['FirstName']
                print(FirstName)
                LastName = row['LastName']
                print(LastName)
                UserID = row['UserID']
                print(UserID)
                Email = row['Email']
                print(Email)
                try:
                    values = (FirstName, LastName, UserID, Email)
                    query = 'INSERT INTO users (FirstName, LastName, UserID, Email) VALUES (%s, %s, %s, %s)'
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
