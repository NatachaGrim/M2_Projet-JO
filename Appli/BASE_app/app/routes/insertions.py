from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import InsertionUsers
from ..utils.transformations import clean_arg
from ..models.users import Users
from .courriel import envoyer_courriel # import de la fonction d'envoi de courriels : à chaque MAJ de la base les notifications seront envoyées 


"""
Route pour l'insertion de nouveaux utilisateurs.

Méthodes acceptées
------------------
GET, POST

Cette route permet à un utilisateur de s'inscrire dans l'application. Elle prend en charge deux méthodes HTTP : GET et POST. En utilisant GET, la page d'inscription est affichée. En utilisant POST, les informations soumises par l'utilisateur sont traitées.

Si l'utilisateur remplit le formulaire d'inscription et soumet ses données (POST), la route vérifie d'abord la validité du formulaire. Si le formulaire est valide, elle tente d'ajouter le nouvel utilisateur à la base de données. 

Si l'ajout est réussi, un message de succès est affiché et un e-mail de notification est envoyé (cette partie devrait être supprimée ou modifiée plus tard pour éviter les spams). L'utilisateur est ensuite redirigé vers la page de connexion.

En cas d'erreur (comme une violation des contraintes de saisie), un message d'erreur est affiché et la transaction est annulée (rollback).

Returns
-------
template
    Rendu de la page d'ajout d'un utilisateur avec un formulaire d'inscription.
"""

@app.route("/insertion/utilisateur", methods=['GET', 'POST'])
def insertion_utilisateur():
    form = InsertionUsers()
    nouvel_utilisateur = ""
    try:
        donnees = [] # Initialiser données comme une liste vide

        if form.validate_on_submit():
            # Nettoyage et récupération des données du formulaire
            mail = clean_arg(request.form.get("mail", None))
            pseudo = clean_arg(request.form.get("pseudo", None))
            mot_de_passe = clean_arg(request.form.get("mot_de_passe", None))

            # Tentative d'ajout du nouvel utilisateur dans la base de données
            if mail and pseudo and mot_de_passe:
                nouvel_utilisateur, erreurs = Users().Ajout(pseudo=pseudo, password=mot_de_passe, mail=mail)
                if nouvel_utilisateur:
                    flash(f"L'utilisateur {nouvel_utilisateur.pseudo} a bien été ajouté dans la base.", 'success')
                    envoyer_courriel()  # Envoi de courriel, à supprimer/modifier ultérieurement pour éviter le spam
                    return redirect(url_for("connexion")) #renvoie à la page de connexion
                else:
                    flash(f"L'utilisateur n'a pas été ajouté dans la base. Erreurs : ", 'error')
        else:
            flash("Merci d'indiquer vos informations de création de compte.", 'info')
    
    except Exception as e:
        # Gestion des erreurs lors de l'ajout de l'utilisateur
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'ajout de l'utilisateur, avez-vous respecté les contraintes de saisie ?" + str(e), 'info')
        db.session.rollback()

    # Rendu de la page avec le formulaire d'inscription
    return render_template("pages/ajout_utilisateur.html", sous_titre="Recherche", donnees=donnees, form=form, nouvel_utilisateur=nouvel_utilisateur)
