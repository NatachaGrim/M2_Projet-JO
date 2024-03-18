from ..app import app, db
from ..utils.email import send_email
from ..models.users import Users
from flask import flash, render_template, redirect, url_for

@app.route("/envoyer_courriel")
def envoyer_courriel():
    # Paramètres du courriel
    subject = "Notification - ajout de pays dans l'appliation Jeux-olympiques"
    sender = "maxime.griveau@chartes.psl.eu"  
    recipients = [user.mail for user in Users.query.filter_by(notifications=True).all()]  #n'envoie de mails que si les notifications sont activitées (le booléen correspondant sera égal à 1 dans la BDD)
    text_body= "test" #on laisse vide 
    html_body = render_template('pages/mails/email-MAJ-BDD.html')

    # Envoi du courriel
    send_email(subject, sender, recipients, text_body, html_body)
    flash("Une notification vient d'être envoyée aux abonnés.", 'success')
    #pas de redirection ici, cette fonction s'active "dans le dos" des utilisateurs
    return redirect(url_for("donnees"))