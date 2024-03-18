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

# Fonction d'envoi de courriel
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

from .routes import generales, insertions, users, favoris, graphiques, courriel, suppressions