import flask
#import flask_jwt
from flask_jwt_extended import JWTManager
import werkzeug

app = flask.Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5000)


@app.route('/')
def root():
    return 'Hi. Good for you you found /'

@app.route('/signup/', methods=['POST'])
def sign_up():
    password = flask.request.json.get('password', None)
    email = flask.request.json.get('email', None)
    firstName = flask.request.json.get('firstName', None)
    lastName = flask.request.json.get('lastName', None)
    response = add_user(firstName,lastName,email,password)
    if response == 0:
        return 'Successful Authentication!'
    elif response == 1:
        return 'Failed to add user.'


@app.route('/login/', methods=['POST']) #TODO
def login():
    email = flask.request.json.get('email', None)
    password = flask.request.json.get('password', None)
    response = authenticate(email,password)
    if response:
        #TODO return access token
        return 'Authenticated!'
    else:
        return flask.jsonify({'Authentication Error': 'Invalid username or password.'})

def authenticate(username,password): #TODO
    return username
    #make call to user DB table for matching creds

def add_user(firstName,lastName,email,password): #TODO
    #check for duplicate emails.IDs if there are no duplicates return 0 else 1.
    return 0


@app.route('/user/<user_id>')
#@flask_jwt.jwt_required()
def view_profile(user_id):
    return user_id
