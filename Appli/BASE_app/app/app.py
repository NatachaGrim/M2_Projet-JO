from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_login import LoginManager
from flask_mail import Mail


from dotenv import load_dotenv
import os

app = Flask(
    __name__, 
    template_folder='templates',
    static_folder='statics')
app.config.from_object(Config)

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
login = LoginManager(app)
mail = Mail(app) #instanciation de la classe Mail 

from .routes import generales, insertions, users, favoris, graphiques, notifications
