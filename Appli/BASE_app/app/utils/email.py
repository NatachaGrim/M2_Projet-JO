from flask_mail import Message
from ..app import mail

def send_email(subject, sender, recipients, text_body, html_body):
    """
    Envoie un e-mail avec le sujet, l'expéditeur, les destinataires, le corps texte et le corps HTML spécifiés.
    """
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
