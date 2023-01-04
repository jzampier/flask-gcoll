"""Flask Game Site"""
from flask import Flask
from flask_mysqldb import MySQL

# ? Instance of Flask class on app
app = Flask(__name__)
# ? app configuration
app.config.from_pyfile('config.py')
# * Database Instance and configuration
db = MySQL(app)
#! Import all routes from our views file (import it after app is instantiated)
from views import *

# ? Grants tha our code isn't executed during modules importing
if __name__ == "__main__":
    app.run(debug=True)
