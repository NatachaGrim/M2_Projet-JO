from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, TextAreaField, validators



class InsertionUsers(FlaskForm):
    mail = StringField("mail", validators=[
        validators.DataRequired(),
        validators.Email(message="Format d'email invalide")
    ])
    pseudo = StringField("pseudo", validators=[validators.Length(min = 3, message="Le pseudo doit être constitué d'au moins trois caractères")])
    mot_de_passe = StringField("mot_de_passe", validators=[validators.Length(min = 6, message="Le mot de passe doit être constitué d'au moins six caractères")])

class Connexion(FlaskForm):
       mail = StringField("mail", validators=[validators.DataRequired(),validators.Email(message="Format d'email invalide")]) 
       mot_de_passe = StringField("mot_de_passe", validators=[validators.Length(min = 6, message="Le mot de passe doit être constitué d'au moins six caractères")])