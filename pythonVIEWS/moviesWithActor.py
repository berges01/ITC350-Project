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
    sql_create_view_query = """ CREATE VIEW `moviesWithActor` AS 
                       SELECT Title
                       FROM movie
                       WHERE VALUES (%s)"""
    # tuple to insert at placeholder
    tuple1 = (actorName)

    cursor.execute(sql_create_view_query, tuple1)
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
