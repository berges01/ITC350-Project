import flask
import mysql.connector
import bcrypt

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
    


@app.route('/user/<user_id>')
#@flask_jwt.jwt_required()
def view_profile(user_id):
    return user_id
