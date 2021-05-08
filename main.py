from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import cProfile
import re

app = Flask(__name__)  # goes above configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videogames.db'

db = SQLAlchemy(app)




from views import *