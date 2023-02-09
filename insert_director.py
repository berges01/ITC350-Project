import mysql.connector
import csv

def main():
    DataBase = CreateConnection()
    CreateCursor(DataBase)

def CreateConnection():     
    DataBase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Viva La Vida2009!",
        database = "movie_mash_schema",
        port = 3306
    )
    return DataBase

def CreateCursor(DataBase):
    with open('./ITC350-Project/data/director_data.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            print(" -------------- Movie -----------------")
            Director_Name = row['Director_Name']
            print(Director_Name)
            Director_ID = row['Director_ID']
            print(Director_ID)
    values = () 
    #values = ('test movie','11-11-2002',1,'test','PG',123,240,'test.com')      
    query = 'INSERT INTO director (Director_Name, Director_ID)'
    cursor = DataBase.cursor()
    cursor.execute(query,values)
    DataBase.commit()
    print(cursor.rowcount, "record inserted.")
    DataBase.close()

if __name__ == "__main__":
    main()