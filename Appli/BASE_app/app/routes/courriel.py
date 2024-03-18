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
def envoyer_courriel():
    # Définir le sujet du courriel.
    subject = "Notification - ajout de pays dans l'appliation Jeux-olympiques"

    # Adresse e-mail de l'expéditeur.
    sender = "maxime.griveau@chartes.psl.eu"  

    # Récupérer les adresses e-mail des utilisateurs ayant activé les notifications.
    # La liste des destinataires est extraite de la base de données.
    recipients = [user.mail for user in Users.query.filter_by(notifications=True).all()]
    
    recipients_pseudos = [user.pseudo for user in Users.query.filter_by(notifications=True).all()]

    # Corps du courriel en texte brut.
    text_body = "test"  # Le corps du texte est ici défini simplement comme 'test' (ne s'affichera pas).

    # Corps du courriel en HTML.
    # Utilise un template HTML pour créer un contenu de courriel formaté.
    html_body = render_template('pages/mails/email-MAJ-BDD.html', pseudo = recipients_pseudos)

    # Appeler la fonction d'envoi de courriel.
    send_email(subject, sender, recipients, text_body, html_body)

    # Afficher un message flash pour confirmer l'envoi du courriel.
    flash("Une notification vient d'être envoyée aux abonnés.", 'success')

    # Rediriger l'utilisateur vers la page 'donnees' après l'envoi du courriel.
    return redirect(url_for("donnees")) 
