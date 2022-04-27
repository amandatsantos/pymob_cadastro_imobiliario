from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:adimin@localhost:5432/Pymobi'
app.config['SECRET_KEY'] = 'random string'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from imob.admin import rotas
from imob.pymobi import rotas
