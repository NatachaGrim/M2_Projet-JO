from ..app import app, db, login
from flask import render_template, request, flash, abort, redirect, url_for, abort 
from ..models.Jeux_Olympiques import Donnees, Formulaire, Medailles, Pays
from ..models.formulaires import InsertionUsers, Connexion
from ..utils.transformations import clean_arg
from ..models.users import Users
from flask_login import current_user, logout_user, login_user
from functools import wraps
from flask import abort


@app.route("/connexion", methods=['GET', 'POST'])
@app.route("/connexion/<int:page>", methods=['GET', 'POST'])
def connexion(page=1):
    """
    Route pour gérer la connexion des utilisateurs.

    Parameters
    ----------
    page : int, optional
        Numéro de la page actuelle, par défaut à 1.

    Returns
    -------
    template
        Retourne le template de la page de connexion avec les données nécessaires.
    """
    form = Connexion()
    try:
        if form.validate_on_submit():
            mot_de_passe = clean_arg(request.form.get("mot_de_passe", None))
            mail = clean_arg(request.form.get("mail", None))
            if not current_user.is_authenticated:
                if mail and mot_de_passe:
                    utilisateur = Users.Identification(password=mot_de_passe, mail=mail)
                    if utilisateur:
                        login_user(utilisateur)
                        if utilisateur.administrateur:
                            flash(f"{utilisateur.mail} est désormais connecté en tant qu'administrateur.", 'success')
                        else:
                            flash(f"{utilisateur.mail} est désormais connecté en tant que journaliste.", 'success')
                    else:
                        flash("Adresse mail ou mot de passe incorrect.", 'error')
                else:
                    flash("Impossible de vous connecter, merci de fournir vos informations de connexion.", 'error')
            else:
                flash("Vous êtes déjà connecté.", 'info')

    except Exception as e:
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de la connexion, avez-vous respecté les contraintes de saisie ?" + str(e), 'info')
        db.session.rollback()

    return render_template("pages/connexion.html", sous_titre="Recherche", form=form)




def admin_required(f): #défini un décorateur "admin_requiered" qui prend une fonction 'f' comme argiment
    @wraps(f) #Ce décorateur permet de s'assurer que les métadonnées de la fonction originales soient inclues dans le décorateur
    def decorated_function(): #décorateur
        if not current_user.administrateur: #Si l'utilisateur n'est pas administrateur 
            abort(403)  # Interdit (renvoie une erreur 403)
        return f() #sinon tout va bien 
    return decorated_function



@app.route("/utilisateurs/deconnexion", methods=["POST", "GET"])
def deconnexion():
    """
    Route pour gérer la déconnexion des utilisateurs.

    Ne retourne rien 
    -------
    redirect
        Redirige vers la page d'accueil après la déconnexion.
    """
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté", "info")
    return redirect(url_for("donnees"))

login.login_view = "connexion"
