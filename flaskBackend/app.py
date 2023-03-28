import flask
import mysql.connector
import bcrypt
import json
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

@app.route('/')
def root():
    return 'Hi. Good for you you found /'

@app.route('/sortmoviesbytitle/', methods=['GET']) #TODO 
def sort_movies_by_title():
    query_string = 'SELECT * FROM selectmovies'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/highlyratedmovies/', methods=['GET']) #TODO
def sort_movies_by():
    query_string = "SELECT * FROM movie_mash.highlyratedmovies"
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/moviesbyreleasedate/', methods=['GET']) #TODO 
def sort_movies_by_release():
    query_string = 'SELECT * FROM movie_mash.moviesbyreleasedate'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/moviesbyruntime/', methods=['GET']) #TODO 
def sort_movies_by_runtime():
    query_string = 'SELECT * FROM movie_mash.moviesbyruntime'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/moviesundertwohours/', methods=['GET']) #TODO MOVIES UNDER TWO HOURS
def get_movies_under_two_hours():
    query_string = 'SELECT * FROM movie_mash.moviesundertwohours'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

#@app.route('/moviesbydirectorname/', methods=['GET']) #TODO MOVIES SORTED BY DIRECTOR NAME - JOSH
#def sort_movies_by_directorname():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesbyrating/', methods=['GET']) #TODO MOVIES SORTED BY RATING - JOSH
#def sort_movies_by_rating()):
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesbygenre/', methods=['GET']) #TODO MOVIES SORTED BY GENRE - JOSH
#def sort_movies_by_genre():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesofgenre/', methods=['GET']) #TODO MOVIES OF PARTICULAR GENRE - JOSH
#def get_movies_of_genre():
    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

@app.route('/specificmovie/', methods=['GET']) #TODO Specific Movie by ID - JONA - STATUS: TEST API
def get_specific_movie():
    movie_id = flask.request.json.get('movie_id', None)
    query_string = 'SELECT * FROM movie_mash.moviessortedbytitle WHERE movie_id = %s'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string, movie_id)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/actorswithdirector/', methods=['GET']) #TODO returns list of directors that have worked with a PARTICULAR actor - JONA - STATUS: TEST API
def get_actors_with_director():
    actor_name = flask.request.json.get('actor_name', None)
    query_string = 'SELECT * FROM movie_mash.actornameswithdirectornames WHERE actor_name = %s'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string, actor_name)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/avgdirectorsmoviesratings/', methods=['GET']) #TODO Average Director's Movies' Ratings - JONA - STATUS: TEST SQL FIRST
def get_avg_directors_movies_ratings():
    director_name = flask.request.json.get('director_name', None)
    query_string = 'SELECT AVG(movie_rating) (SELECT * FROM movie_mash.averageratingofmoviebydirector WHERE director_name = %s)' #DO WE NEED MORE FIELDS
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string, director_name)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/avgactorsmoviesratings/', methods=['GET']) #TODO Average Actor's Movies' Ratings - JONA - STATUS: TEST SQL FIRST
def get_avg_actors_movies_ratings():
    actor_name = flask.request.json.get('actor_name', None)
    query_string = 'SELECT AVG(movie_rating) (SELECT * FROM movie_mash.averageratingofmoviewithactor WHERE actor_name = %s)' #DO WE NEED MORE FIELDS
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string, actor_name)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/actorsawards/', methods=['GET']) #TODO Return a particular Actor with their movies' awards - JONA - STATUS: TEST API
def get_actors_movies_awards():
    actor_name = flask.request.json.get('actor_name', None)
    query_string = 'SELECT * FROM movie_mash.actornameswithawardnames WHERE actor_name = %s'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string, actor_name)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

#@app.route('/directorsmovies/', methods=['GET']) #TODO returns all movies by a particular director - JAKE
#def get_directors_movies():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/movieawards/', methods=['GET']) #TODO get awards for a particular movie - JAKE
#def get_movie_awards():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

#@app.route('/moviesofcontentrating/', methods=['GET']) #TODO - JAKE 
#def get_movies_with_content_rating():

    #query_string = ''
    #cursor = DataBase.cursor(prepared=True)
    #cursor.execute(query_string)
    #data = cursor.fetchall()

@app.route('/moviesreleasedbetween/', methods=['GET']) #TODO Return movies between two dates - JAKE
def get_movies_between():
    start_year = flask.request.json.get('date1', None)
    end_year = flask.request.json.get('date2', None)
    range = [start_year, end_year]
    query = "SELECT * FROM movie_mash.selectmovies WHERE Release_Year BETWEEN %s AND %s;"
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query,range)
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/favoritedbyme/', methods=['GET']) #TODO RETURN MOVIES FAVORITED BY ME - JAKE
def get_my_favorites():
    user_id = flask.request.json.get('user_id', None)
    query_string = 'SELECT Title FROM movie_mash.favoritedmoviesformatted WHERE Email = %s'
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query_string, [user_id])
    data = cursor.fetchall()
    json_result = format_response(data,cursor)
    return json_result

@app.route('/signup/', methods=['POST'])
def sign_up():
    password = flask.request.json.get('password', None)
    encoded_pw = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashPass = bcrypt.hashpw(encoded_pw,salt)
    hashPass_decoded = hashPass.decode("utf-8")
    email = flask.request.json.get('email', None)
    firstName = flask.request.json.get('firstName', None)
    lastName = flask.request.json.get('lastName', None)
    response = add_user(firstName,lastName,email,hashPass_decoded)
    if response == 0:
        return email + ' successfully joined Movie Mash! Please Return to login page to sign in.'
    elif response == 1:
        return 'Failed to add user. Duplicate entry found for email ' + email


@app.route('/login/', methods=['POST']) #TODO
def login():
    email = flask.request.json.get('email', None)
    password = flask.request.json.get('password', None)
    response = authenticate(email,password)
    if response == True:
        return email
    elif response == False:
        return flask.jsonify({'Authentication Error': 'Invalid username or password.'})


def authenticate(email,password): #TODO
    password = password.encode("utf-8")
    query = "SELECT Passwd FROM movie_mash.users WHERE email = %s"
    cursor = DataBase.cursor(prepared=True)
    cursor.execute(query, [email])
    result = cursor.fetchone()
    if result is None:
        print('User not found.')
        return False
    else:
        stored_hash = result[0].encode("utf-8")
        if bcrypt.checkpw(password, stored_hash):
            return True
        else:
            return False
        
        
def add_user(firstName,lastName,email,password): #TODO
    #check for duplicate emails.IDs if there are no duplicates return 0 else 1.
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
    
@app.route('/user/<user_id>')  #TODO - JAKE
def view_profile(user_id):
    return user_id
