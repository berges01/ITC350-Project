import mysql.connector

try:
    DataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Viva La Vida2009!",
        database="movie_mash",
        port=3306
    )

    cursor = DataBase.cursor(prepared=True)
    # Parameterized query
    sql_insert_query = """ INSERT INTO Employee
                       (id, Name, Joining_date, salary) VALUES (%s,%s,%s,%s)"""
    # tuple to insert at placeholder
    tuple1 = (1, "Json", "2019-03-23", 9000)
    tuple2 = (2, "Emma", "2019-05-19", 9500)

    cursor.execute(sql_insert_query, tuple1)
    cursor.execute(sql_insert_query, tuple2)
    connection.commit()
    print("Data inserted successfully into employee table using the prepared statement")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


if __name__ == "__main__":
    main()
