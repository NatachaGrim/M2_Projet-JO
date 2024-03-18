from ..app import app, db
from flask import render_template, request, flash, redirect, url_for, abort
from sqlalchemy import or_
from ..models.Jeux_Olympiques import Pays, Donnees, Formulaire, Medailles, Favoris
from flask_login import current_user, logout_user, login_user, login_required
from .generales import donnees_pays
from ..models.users import Users


"""
Route pour ajouter un pays aux favoris.

Cette route ajoute le pays spécifié, identifié par son 'nom_pays', à la liste des favoris de l'utilisateur connecté. 
Le pays est ajouté indépendamment de l'année, l'important étant que le code NOC soit correct.

Méthodes acceptées
------------------
POST

Parameters
----------
nom_pays : str
    Le nom du pays à ajouter aux favoris.

Returns
-------
redirect
    Redirige vers la page 'donnees_pays' avec le nom du pays ajouté ou vers la page d'accueil si une erreur survient.
"""

@app.route('/ajouter_favoris/<nom_pays>', methods=['GET', 'POST'])
@login_required

def ajouter_favoris(nom_pays):
    try:
        # Trouver le pays en utilisant le nom du pays pour vérifier qu'il existe bel et bien dans la base (normalement oui sinon la page "données_pays" ne serait pas générée)
        pays = Pays.query.filter(Pays.nom == nom_pays).first()
        if not pays:
            flash("Pays non trouvé.", "error")
            return redirect(url_for('index'))
        # On utilise filter_by et non filter, car celui-ci est plus recommandé dans le cas de conditions simples comme c'est le cas dans notre code (source : https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy )
        # Trouver l'id_team (id unique des pays) en utilisant le NOC du pays (qui est la clé étrangère des deux tables pour faire jointure)
        formulaire = Formulaire.query.filter_by(noc=pays.noc).first()

        
        if not formulaire:
            flash("Identifiant du pays non trouvé", "error")
            return redirect(url_for('index'))

        # Vérifier si l'équipe est déjà en favoris pour cet utilisateur
        # Ici on utilise filter car il y a deux arguments
        favori_exist = Favoris.query.filter(Favoris.id_user == current_user.id, Favoris.id_team == formulaire.id_team).first()

        if favori_exist:
            flash("Cette équipe est déjà dans vos favoris.", "info")
        else:
            # Ajouter l'équipe aux favoris
            nouveau_favori = Favoris(id_user=current_user.id, id_team=formulaire.id_team)
            db.session.add(nouveau_favori)
            db.session.commit()
            flash("Équipe ajoutée aux favoris.", "success")
    #Si l'opération ne se passe pas bien (cas imprévu, on rolleback la base et informe l'utilisateur)
    except Exception as e:
        flash("L'ajout en favoris a rencontré une erreur "+ str(e), "info")
        db.session.rollback()

    return redirect(url_for('donnees_pays', nom_pays=nom_pays))

"""
Route pour afficher les favoris de l'utilisateur connecté.

Cette route récupère et affiche les pays favoris de l'utilisateur connecté. 
Elle récupère les identifiants des équipes favorites (id_team) de l'utilisateur, 
puis trouve les noms de pays correspondants.

Méthodes acceptées
------------------
GET

Returns
-------
template
    Retourne le template 'pages/favoris.html' avec la liste des pays favoris de l'utilisateur.
"""

@app.route('/favoris')
@login_required
def favoris():
    # Récupérer les favoris de l'utilisateur actuel
    favoris_utilisateur = Favoris.query.filter_by(id_user=current_user.id).all()

    # Récupérer les informations détaillées pour chaque favori
    equipes_favorites = []
    for favori in favoris_utilisateur:
        equipe = Formulaire.query.filter_by(id_team=favori.id_team).first()
        if equipe:
            pays = Pays.query.filter_by(noc=equipe.noc).first()
            if pays:
               equipes_favorites.append(pays.nom)

    return render_template("pages/compte-utilisateur/favoris.html", equipes_favorites=equipes_favorites)
    
        


"""
Route pour gérer les préférences de notifications de l'utilisateur.

Méthodes acceptées
------------------
GET, POST

Cette route permet aux utilisateurs de modifier leurs préférences en matière de notifications. L'utilisateur peut choisir de recevoir ou non des notifications par e-mail. 

Lorsque la méthode est POST, la préférence de notification de l'utilisateur est mise à jour en fonction de son choix. Si la méthode est GET, la page de paramétrage des notifications est simplement rendue.

L'accès à cette route est restreint aux utilisateurs connectés.

Returns
-------
template
    Rendu de la page de préférences de notifications avec les informations actuelles de l'utilisateur.
"""

@app.route('/notifications', methods=['GET', 'POST'])
@login_required  # Accès restreint aux utilisateurs authentifiés
def notifications():
    if request.method == 'POST':
        # Récupération du choix de l'utilisateur depuis le formulaire
        choix_notifications = request.form.get('notifications') 

        # Mise à jour des préférences de notifications de l'utilisateur
        # Si le choix est 'on', les notifications sont activées. Sinon, elles sont désactivées.
        current_user.notifications = True if choix_notifications == 'on' else False

        # Sauvegarde des modifications dans la base de données
        db.session.commit()

        # Afficher un message de confirmation
        flash('Vos préférences ont été mises à jour.', 'success')

    # Rendre la page de préférences de notifications avec les informations de l'utilisateur actuel
    return render_template('pages/compte-utilisateur/notifications.html', user=current_user)
