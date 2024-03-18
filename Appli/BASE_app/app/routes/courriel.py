from flask import render_template, jsonify, request
from ..app import app, db
from ..models.Jeux_Olympiques import Pays, Donnees, Formulaire, Medailles
import json
from ..utils.email import send_email
from ..models.users import Users

@app.route("/envoyer_courriel")
def envoyer_courriel():
    # Paramètres du courriel
    subject = "Notification - ajout de pays dans l'appliation Jeux-olympiques"
    sender = "maxime.griveau@chartes.psl.eu"  
    recipients = [user.mail for user in Users.query.filter_by(notifications=True).all()]  #n'envoie de mails que si les notifications sont activitées (le booléen correspondant sera égal à 1 dans la BDD)
    text_body= "test"
    html_body = render_template('pages/mails/email-MAJ-BDD.html')

    # Envoi du courriel
    send_email(subject, sender, recipients, text_body, html_body)

    # Redirection vers une page de confirmation ou une autre action
    return render_template("pages/confirmation-mails.html")
