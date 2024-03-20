from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import SuppressionPays, SuppressionEdition
from ..utils.transformations import clean_arg
from flask_login import current_user, logout_user, login_user, login_required
from ..models.users import Users
from .users import admin_required

@app.route("/suppression/pays", methods=['GET', 'POST'])
@login_required
@admin_required #il faut être administrateur pour pouvoir modifier la base;
def suppression_pays():
    """
    Route permettant la suppression de l'intégralité des données sur un pays. Soit ses informations
    dans l'intégralité des tables de la base de données

    L'utilisateur doit être connecté et avoir le rôle d'administrateur pour effectuer une suppression 
    via le formulaire de la page

    Parameters
    ----------
    None

    Returns
    -------
    template
        Retourne le même template suppression_pays.html avec un message flash en fonction du déroulement 
        de l'ajout
    """
    form = SuppressionPays() # Récupération des données saisies dans le formulaire

    # Requête permettant d'afficher une liste des pays disponibles à l'utilisateur
    liste_pays = Pays.query.all()
    form.nom_pays.choices = [('')] + [(p.nom) for p in liste_pays]

    try:
        if form.validate_on_submit(): # Récupération de l'ensemble des données concernées par l'édition et le pays indiqués
            nom_pays =  clean_arg(request.form.get("nom_pays", None))

            donnees_pays = Pays.query.filter_by(nom=nom_pays).first()
            code_pays = donnees_pays.noc

            donnees_formulaire = Formulaire.query.filter(Formulaire.id_team.like(f"{code_pays} - %")).all()
            donnees_donnees = Donnees.query.filter(Donnees.id_team.like(f"{code_pays} - %")).all()
            donnees_medailles = Medailles.query.filter(Medailles.id_team.like(f"{code_pays} - %")).all()

            # Suppression des données récupérées
            if donnees_pays:
                db.session.delete(donnees_pays)
            
            if donnees_formulaire:
                for donnee in donnees_formulaire:
                    db.session.delete(donnee)

            if donnees_donnees:
                for donnee in donnees_donnees:
                    db.session.delete(donnee)
            
            if donnees_medailles:
                for donnee in donnees_medailles:
                    db.session.delete(donnee)

            db.session.commit()
            flash("La suppression des données sur le pays " + nom_pays + " s'est correctement déroulée", 'success')

    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'insertion des données sur le pays " + nom_pays + " : " + str(e), "error")
        db.session.rollback()
    
    return render_template("pages/suppression_pays.html", sous_titre="Suppression pays", form=form)

@app.route("/suppression/edition", methods=['GET', 'POST'])
@login_required
@admin_required
def suppression_edition():
    """
    Route permettant la suppression des données sur un pays pour une édition donnée. Les données 
    supprimées concernent les tables où est indiquée l'édition à laquelle le pays a participé

    L'utilisateur doit être connecté et avoir le rôle d'administrateur pour effectuer une suppression 
    via le formulaire de la page

    Parameters
    ----------
    None

    Returns
    -------
    template
        Retourne le même template suppression_edition.html avec un message flash en fonction du déroulement 
        de l'ajout
    """
    form = SuppressionEdition() # Récupération des données saisies dans le formulaire

    # Requête permettant d'afficher une liste des pays disponibles à l'utilisateur
    liste_pays = Pays.query.all()
    form.nom_pays.choices = [('')] + [(p.nom) for p in liste_pays]

    try:
        if form.validate_on_submit(): # Récupération de l'ensemble des données concernées par l'édition et le pays indiqués
            nom_pays =  clean_arg(request.form.get("nom_pays", None))
            annee_participation = clean_arg(request.form.get("annee_participation", None))

            donnees_pays = Pays.query.filter_by(nom=nom_pays).first()
            code_pays = donnees_pays.noc
            clef_p=f"{code_pays} - {annee_participation}"

            donnees_formulaire = Formulaire.query.filter_by(id_team=clef_p).first()
            donnees_donnees = Donnees.query.filter_by(id_team=clef_p).first()
            donnees_medailles = Medailles.query.filter_by(id_team=clef_p).first()
            
            # Suppression des données récupérées
            if donnees_formulaire:
                db.session.delete(donnees_formulaire)

            if donnees_donnees:
                db.session.delete(donnees_donnees)
            
            if donnees_medailles:
                db.session.delete(donnees_medailles)

            db.session.commit()

            flash("La suppression des données sur le pays " + nom_pays + " pour l'édition " + annee_participation + " s'est correctement déroulée", 'success')

    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'insertion des données sur le pays " + nom_pays + " pour l'année " + annee_participation + " : " + str(e), "error")
        db.session.rollback()

    return render_template("pages/suppression_edition.html", sous_titre="Suppression édition", form=form)