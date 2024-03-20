from ..app import app, db
from ..utils.email import send_email
from ..models.users import Users
from flask import flash, render_template, redirect, url_for


"""
Route pour envoyer un courriel de notification aux utilisateurs.

Méthodes acceptées
------------------
GET

Cette route est utilisée pour envoyer des notifications par courriel aux utilisateurs qui ont activé cette option dans leurs paramètres. Le courriel contient des informations sur l'ajout de nouveaux pays dans l'application Jeux-olympiques.

Returns
-------
redirect
    Redirige l'utilisateur vers la page de données après l'envoi du courriel.
"""

@app.route("/envoyer_courriel")
def envoyer_courriel(nom):
    subject = "Notification - ajout de pays dans l'application Jeux-olympiques"
    sender = "maxime.griveau@chartes.psl.eu"
    users = Users.query.filter_by(notifications=True).all()

    for user in users:
        recipient = user.mail
        pseudo = user.pseudo

        html_body = render_template('pages/mails/email-MAJ-BDD.html', pseudo=pseudo, nom=nom)
        send_email(subject, sender, [recipient], "test", html_body)

    flash("Une notification vient d'être envoyée aux abonnés.", 'success')
    return redirect(url_for("donnees"))
