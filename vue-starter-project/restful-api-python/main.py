import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

# @app.route('/create', methods=['POST'])
# def create_emp():
#     try:        
#         _json = request.json
#         _name = _json['name']
#         _email = _json['email']
#         _phone = _json['phone']
#         _address = _json['address']	
#         if _name and _email and _phone and _address and request.method == 'POST':
#             conn = mysql.connect()
#             cursor = conn.cursor(pymysql.cursors.DictCursor)		
#             sqlQuery = "INSERT INTO emp(name, email, phone, address) VALUES(%s, %s, %s, %s)"
#             bindData = (_name, _email, _phone, _address)            
#             cursor.execute(sqlQuery, bindData)
#             conn.commit()
#             respone = jsonify('Employee added successfully!')
#             respone.status_code = 200
#             return respone
#         else:
#             return showMessage()
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conn.close()          
     
@app.route('/movie')
def movie():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM movie")
        movieRows = cursor.fetchall()
        response = jsonify(movieRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/movie/<int:Movie_ID>')
def movie_details(Movie_ID):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        print("test")
        cursor.execute("SELECT * FROM movie WHERE Movie_ID =%s", Movie_ID)
        print("test2")
        movieRow = cursor.fetchone()
        response = jsonify(movieRow)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

# not working yet
@app.route('/favorited_uid=<int:___>')
def favorited(____):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM movie WHERE ____")
        movieRows = cursor.fetchall()
        response = jsonify(movieRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/release_year')
def release_year():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM movie ORDER BY Release_Year ASC;")
        movieRows = cursor.fetchall()
        response = jsonify(movieRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/run_time')
def run_time():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM movie ORDER BY Running_Time_Minutes ASC;")
        movieRows = cursor.fetchall()
        response = jsonify(movieRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/genre=<string:Genre>')
def genre(Genre):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM movie WHERE Genre = %s", Genre)
        movieRows = cursor.fetchall()
        response = jsonify(movieRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

# @app.route('/update', methods=['PUT'])
# def update_emp():
#     try:
#         _json = request.json
#         _id = _json['id']
#         _name = _json['name']
#         _email = _json['email']
#         _phone = _json['phone']
#         _address = _json['address']
#         if _name and _email and _phone and _address and _id and request.method == 'PUT':			
#             sqlQuery = "UPDATE movie SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
#             bindData = (_name, _email, _phone, _address, _id,)
#             conn = mysql.connect()
#             cursor = conn.cursor()
#             cursor.execute(sqlQuery, bindData)
#             conn.commit()
#             respone = jsonify('Movie updated successfully!')
#             respone.status_code = 200
#             return respone
#         else:
#             return showMessage()
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conn.close()

@app.route('/delete/', methods=['DELETE'])
def delete_emp(Movie_ID):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM movie WHERE Movie_ID =%s", (Movie_ID,))
		conn.commit()
		response = jsonify('Movie deleted successfully!')
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response
        
if __name__ == "__main__":
    app.run()