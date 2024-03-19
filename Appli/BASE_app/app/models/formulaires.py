from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, TextAreaField, FloatField, IntegerField, validators

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

class AjoutAll(FlaskForm):
    code_pays = StringField("code_pays", validators=[
        validators.DataRequired(),validators.Length(min = 3, max = 3, message="Le code NOC comprend exactement trois caractères"),
        validators.Regexp('^[A-Z]{3}$', message="Le code NOC doit être en majuscules")
    ])
    nom_pays = StringField("nom_pays", validators=[
        validators.DataRequired(),
        validators.Regexp('^[A-Z][a-zA-Z]*$', message="Le nom du pays doit commencer par une majuscule")
    ])
    latitude_pays = FloatField("latitude_pays", validators=[
         validators.DataRequired(),
         validators.NumberRange(min = -90, max = 90, message="La latitude doit être comprise entre -90 et 90 degrés")])
    longitude_pays = FloatField("longitude_pays", validators=[
         validators.DataRequired(),
         validators.NumberRange(min = -180, max = 180, message="La longitude doit être comprise entre -180 et 180 degrés")])
    annee_participation = StringField("annee_participation", validators=[
        validators.DataRequired(),
        validators.Regexp('^\d{4}$', message="Le format de l'année est YYYY")
    ])
    population_pays = IntegerField("population_pays", validators=[
        validators.Optional(),
        validators.NumberRange(min=None, message="La population doit correspondre à un entier")
    ])
    richesse_pays = IntegerField("richesse_pays", validators=[
        validators.Optional(),
        validators.NumberRange(min=None, max=None, message="La richesse doit correspondre à un entier, arrondir au besoin")
    ])
    investissement_pays = FloatField("investissement_pays", validators=[
        validators.Optional(),
        validators.NumberRange(min=None, max=None)
    ])
    gold = IntegerField("gold", validators=[
        validators.DataRequired(message="Ce champ est obligatoire. Si aucune médaille n'a été remportée, indiquer 0"),
        validators.NumberRange(min=0, max=None)
    ])
    silver = IntegerField("silver", validators=[
        validators.DataRequired(message="Ce champ est obligatoire. Si aucune médaille n'a été remportée, indiquer 0"),
        validators.NumberRange(min=0, max=None)
    ])
    bronze = IntegerField("bronze", validators=[
        validators.DataRequired(message="Ce champ est obligatoire. Si aucune médaille n'a été remportée, indiquer 0"),
        validators.NumberRange(min=0, max=None)
    ])
    
class SuppressionPays(FlaskForm):
    nom_pays = SelectField("nom_pays", choices=[])

class SuppressionEdition(FlaskForm):
    nom_pays = SelectField("nom_pays", choices=[])
    annee_participation = SelectField("annee_participation", choices=[(''), ('1996'), ('2000'), ('2004'), ('2008'), ('2012'), ('2016')])