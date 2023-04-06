from app import app
from flaskext.mysql import MySQL
from dotenv import load_dotenv
import os
load_dotenv()

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get("passwd")
app.config['MYSQL_DATABASE_DB'] = 'movie_mash'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)