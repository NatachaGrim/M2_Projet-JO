from flask import Flask
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_login import LoginManager

app = Flask(
    __name__, 
    template_folder='templates',
    static_folder='statics')
app.config.from_object(Config)

db = SQLAlchemy(app)

# Initialisez ici l'extension Mail
mail = Mail(app)

login = LoginManager(app)

from .routes import generales, insertions, users, graphiques, courriel, compte_utilisateur, suppressions, editions, erreurs


