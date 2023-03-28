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

@app.route('/sortmoviesbytitle/', methods=['GET']) #TODO DO FINAL TESTS
def sort_movies_by_title():
    query_string = 'SELECT * FROM selectmovies'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

#@app.route('/highlyratedmovies/', methods=['GET']) #TODO HIGHLY RATED MOVIES
#def get_highly_rated_movies():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesbyreleasedate/', methods=['GET']) #TODO MOVIES SORTED BY RELEASE DATE
#def sort_movies_by_release():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesbyruntime/', methods=['GET']) #TODO MOVIES SORTED BY RUNTIME
#def sort_movies_by_runtime():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesundertwohours/', methods=['GET']) #TODO MOVIES UNDER TWO HOURS
#def get_movies_under_two_hours():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesbydirectorname/', methods=['GET']) #TODO MOVIES SORTED BY DIRECTOR NAME
#def sort_movies_by_directorname():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesbyrating/', methods=['GET']) #TODO MOVIES SORTED BY RATING
#def sort_movies_by_rating()):
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesbygenre/', methods=['GET']) #TODO MOVIES SORTED BY GENRE
#def sort_movies_by_genre():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesofgenre/', methods=['GET']) #TODO MOVIES OF PARTICULAR GENRE
#def get_movies_of_genre():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/specificmovie/', methods=['GET']) #TODO Specific Movie by ID
#def get_specific_movie():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/actorswithdirector/', methods=['GET']) #TODO returns list of directors that have worked with a specified actor
#def get_actors_with_director():
    #actor_id = flask.request.json.get('actor_id', None)

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/avgdirectorsmoviesratings/', methods=['GET']) #TODO Average Director's Movies' Ratings !!!!!!
#def get_avg_directors_movies_ratings():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/avgactorsmoviesratings/', methods=['GET']) #TODO Average Actor's Movies' Ratings !!!!!!
#def get_avg_actors_movies_ratings():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/actorsawards/', methods=['GET']) #TODO Return an Actor with their movies' awards
#def get_actors_movies_awards():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/directorsmovies/', methods=['GET']) #TODO returns all movies by a particular director
#def get_directors_movies():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/movieawards/', methods=['GET']) #TODO get awards for a particular movie
#def get_movie_awards():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesofcontentrating/', methods=['GET']) #TODO 
#def get_movies_with_content_rating():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesreleasedbetween/', methods=['GET']) #TODO Return mvoies between two dates - TAKE INPUT
#def get_movies_between():
    #date1 = flask.request.json.get('', None)
    #date2 = flask.request.json.get('', None)

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/favoritedbyme/', methods=['GET']) #TODO RETURN MOVIES FAVORITED BY ME
#def get_my_favorites():
    #user_id = flask.request.json.get('user_id', None)

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

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
