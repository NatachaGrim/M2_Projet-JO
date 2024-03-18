from flask import render_template, jsonify, request
from ..app import app, db
from ..models.Jeux_Olympiques import Pays, Donnees, Formulaire, Medailles
import json
from ..utils.email import send_email

@app.route("/envoyer_courriel")
def envoyer_courriel():
    # Paramètres du courriel
    subject = "Test d'envoi de courriel"
    sender = "estchlrcq@yahoo.com"  # Remplacez par votre adresse e-mail Yahoo
    recipients = ["theo.burnel@gmail.com"]  # Adresse e-mail du destinataire
    text_body = "Ceci est un test d'envoi de courriel."
    html_body = render_template('pages/email.html')

    # Envoi du courriel
    send_email(subject, sender, recipients, text_body, html_body)

    # Redirection vers une page de confirmation ou une autre action
    return render_template("pages/essai.html")
