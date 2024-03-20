from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import EditionSelection, EditionAjout
from ..utils.transformations import clean_arg
from flask_login import current_user, logout_user, login_user, login_required
from ..models.users import Users
from .users import admin_required

@app.route("/edition/selection", methods=['GET', 'POST'])
@login_required
@admin_required
def edition_selection():
    """
    Route préliminaire à l'édition de données sur une édition des Jeux Olympiques à laquelle
    a participé un pays donné

    L'utilisateur doit être connecté et avoir le rôle d'administrateur pour pouvoir sélectionner
    le nom du pays et l'année afin de modifier les données

    Parameters
    ----------
    None

    Returns
    -------
    template
        Retourne le template edition_ajout.html, lequel contient un formulaire permettant
        d'éditer les données du pays sélectionné, pour l'année sélectionnée

    Raises
    ------
    404 Not Found
        Si une ressource nécessaire (comme la liste des pays) n'est pas trouvée.
    500 Internal Server Error
        Si une erreur inattendue se produit lors du traitement du formulaire.
    """
    form = EditionSelection() # Récupération des données saisies dans le formulaire

    # Requête permettant d'afficher une liste des pays disponibles à l'utilisateur
    liste_pays = Pays.query.all()
    form.nom_pays.choices = [('')] + [(p.nom) for p in liste_pays]

    try:
        if form.validate_on_submit(): # Redirection vers la page d'édition en fonction des choix
            nom_pays =  clean_arg(request.form.get("nom_pays", None))
            annee_participation =  clean_arg(request.form.get("annee_participation", None))
            return redirect(url_for('edition_ajout', nom_pays=nom_pays, annee_participation=annee_participation))
    
    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de la sélection du pays " + nom_pays + " : " + str(e), "error")
        db.session.rollback()
        abort(500)

    return render_template("pages/edition_selection.html", sous_titre="Édition données", form=form)

@app.route("/edition/<nom_pays>/<annee_participation>", methods=['GET', 'POST'])
@login_required
def edition_ajout(nom_pays, annee_participation):
    """
    Route permettant d'éiter les données d'un pays pour une édition des Jeux Olympiques
    sélectionnée par l'utilisateur

    L'utilisateur doit être connecté pour soumettre le formulaire

    Parameters
    ----------
    nom_pays : str
        Le nom du pays dont éditer les données
    annee_participation : str
        L'année de participation dont éditer les données

    Returns
    -------
    template
        Retourne le même template edition_ajout.html avec un message flash en fonction
        du déroulement de la modification

    Raises
    ------
    500 Internal Server Error
        Si une erreur inattendue se produit lors du traitement du formulaire.
    """
    # Récupération des données existantes en base
    donnees_pays = Pays.query.filter_by(nom=nom_pays).first()
    code_pays = donnees_pays.noc
    clef_p=f"{code_pays} - {annee_participation}"
    donnees_donnees = Donnees.query.filter_by(id_team=clef_p).first()
    donnees_medailles = Medailles.query.filter_by(id_team=clef_p).first()
    
    form = EditionAjout() # Récupération des données saisies dans le formulaire

    try:
        if form.validate_on_submit(): # Modification des données

            if form.population_pays.data is not None:
                donnees_donnees.population = form.population_pays.data

            if form.richesse_pays.data is not None:
                donnees_donnees.richesse = form.richesse_pays.data

            if form.investissement_pays.data is not None:
                donnees_donnees.investissement = form.investissement_pays.data

            if form.gold.data is not None:
                donnees_medailles.gold_count = form.gold.data

            if form.silver.data is not None:
                donnees_medailles.silver_count = form.silver.data

            if form.bronze.data is not None:
                donnees_medailles.bronze_count = form.bronze.data

            # Calcul automatique du total des médailles
            donnees_medailles.total = int(donnees_medailles.gold_count) + int(donnees_medailles.silver_count) + int(donnees_medailles.bronze_count)
            
            db.session.commit()
            flash("La modification des données sur le pays " + nom_pays + " pour l'édition " + annee_participation + " s'est correctement déroulée", 'success')

    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de la modification des données sur le pays " + nom_pays + " pour l'année " + annee_participation + " : " + str(e), "error")
        db.session.rollback()
        abort(500)

    return render_template("pages/edition_ajout.html", form=form, nom_pays=nom_pays, annee_participation=annee_participation, donnees_donnees=donnees_donnees, donnees_medailles=donnees_medailles)