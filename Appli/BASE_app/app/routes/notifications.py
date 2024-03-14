from ..app import app, db, mail
from flask import render_template, request, flash, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Formulaire, Medailles, Favoris
from flask_login import LoginManager, login_required 
from .users import admin_required 
from flask_mail import Mail, Message



@app.route('/update', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipient = request.form['recipient']
        msg = Message('Twilio SendGrid Test Email', recipients=[recipient])
        msg.body = ('Congratulations! You have sent a test email with '
                    'Twilio SendGrid!')
        msg.html = ('<h1>Twilio SendGrid Test Email</h1>'
                    '<p>Congratulations! You have sent a test email with '
                    '<b>Twilio SendGrid</b>!</p>')
        mail.send(msg)
        flash(f'A test message was sent to {recipient}.')
        return redirect(url_for('index'))
    return render_template('pages/notifications.html')