import flask
import mysql.connector
import bcrypt
import json
import flask_jwt
from flask_jwt_extended import JWTManager
import werkzeug

#GLOBAL VARS
app = flask.Flask(__name__)
DataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Viva La Vida2009!",
    database="movie_mash",
    port=3306
)
salt = bcrypt.gensalt()

@app.route('/')
def root():
    return 'Hi. Good for you you found /'

@app.route('/sortmoviesbytitle/', methods=['GET']) #TODO Jona - works without jsonify but need to figure out how to return as JSON for frontend simplicity
def sort_movies_by_title():
    query_string = 'SELECT * FROM selectmovies'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

#@app.route('/highlyratedmovies/', methods=['GET']) #TODO HIGHLY RATED MOVIES
#def sort_movies_by():

#@app.route('/moviesbyreleasedate/', methods=['GET']) #TODO MOVIES SORTED BY RELEASE DATE
#def sort_movies_by():

#@app.route('/moviesbyruntime/', methods=['GET']) #TODO MOVIES SORTED BY RUNTIME
#def sort_movies_by():

#@app.route('/moviesundertwohours/', methods=['GET']) #TODO MOVIES UNDER TWO HOURS
#def sort_movies_by():

#@app.route('/moviesbydirectorname/', methods=['GET']) #TODO MOVIES SORTED BY DIRECTOR NAME
#def sort_movies_by():

#@app.route('', methods=['GET']) #TODO MOVIES SORTED BY RATING
#def sort_movies_by():

#@app.route('', methods=['GET']) #TODO MOVIES SORTED BY GENRE
#def sort_movies_by():

#@app.route('', methods=['GET']) #TODO
#def sort_movies_by():

@app.route('/signup/', methods=['POST'])
def sign_up():
    password = flask.request.json.get('password', None)
    hashPass = bcrypt.hashpw(password.encode('utf-8'),salt)
    email = flask.request.json.get('email', None)
    firstName = flask.request.json.get('firstName', None)
    lastName = flask.request.json.get('lastName', None)
    response = add_user(firstName,lastName,email,hashPass)
    if response == 0:
        return email + ' successfully joined Movie Mash!'
    elif response == 1:
        return 'Failed to add user.'


@app.route('/login/', methods=['POST']) #TODO
def login():
    email = flask.request.json.get('email', None)
    password = flask.request.json.get('password', None)
    response = authenticate(email,password)
    if response:
        #TODO return access token or IDentity 
        return 'Authenticated!'
    else:
        return flask.jsonify({'Authentication Error': 'Invalid username or password.'})



def authenticate(username,password): #TODO
    return username
    #make call to user DB table for matching creds

def add_user(firstName,lastName,email,password): #TODO
    #check for duplicate emails.IDs if there are no duplicates return 0 else 1.4
    try:
        values = (firstName, lastName, email, password)
        query = 'INSERT INTO users (FirstName, LastName, Email, Passwd) VALUES (%s, %s, %s, %s)'
        cursor = DataBase.cursor(prepared=True)
        cursor.execute(query, values)
        DataBase.commit()
        print(cursor.rowcount, "record inserted.")
        return 0
    except Exception as insert_error:
        print("DB Insertion Error: %s" % insert_error)
        return 1
    
def format_response(data,cursor):
    result_list = []
    for row in data:
        result_dict = {}
        for i in range(len(cursor.description)):
            result_dict[cursor.description[i][0]] = row[i]
        result_list.append(result_dict)
    # convert the result list to a JSON string
    result_json = json.dumps(result_list)
    # return the JSON string in the response
    return result_json
    
@app.route('/user/<user_id>')
#@flask_jwt.jwt_required()
def view_profile(user_id):
    return user_id
