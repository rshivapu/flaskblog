from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '231cc16d13eb5311d1e568b3de141393'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes