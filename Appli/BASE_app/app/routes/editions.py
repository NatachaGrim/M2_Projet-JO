from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import EditionDonnees, EditionAjout
from ..utils.transformations import clean_arg
from flask_login import current_user, logout_user, login_user, login_required
from ..models.users import Users
from .users import admin_required

@app.route("/edition/donnees", methods=['GET', 'POST'])
@login_required
#@admin_required
def edition_donnees():
    form = EditionDonnees()

    liste_pays = Pays.query.all()
    form.nom_pays.choices = [('')] + [(p.nom) for p in liste_pays]

    try:
        if form.validate_on_submit():
            nom_pays =  clean_arg(request.form.get("nom_pays", None))
            annee_participation =  clean_arg(request.form.get("annee_participation", None))
            
            return redirect(url_for('edition_ajout', nom_pays=nom_pays, annee_participation=annee_participation))
    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de la sélection du pays " + nom_pays + " : " + str(e), "error")
        db.session.rollback()
    
    return render_template("pages/edition_donnees.html", sous_titre="Édition données", form=form)



@app.route("/edition/<nom_pays>/<annee_participation>", methods=['GET', 'POST'])
@login_required
def edition_ajout(nom_pays, annee_participation):

    donnees_pays = Pays.query.filter_by(nom=nom_pays).first()
    code_pays = donnees_pays.noc
    clef_p=f"{code_pays} - {annee_participation}"

    donnees_donnees = Donnees.query.filter_by(id_team=clef_p).first()
    donnees_medailles = Medailles.query.filter_by(id_team=clef_p).first()
    
    print("ok1")

    form = EditionAjout()

    try:
        if form.validate_on_submit():

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

            donnees_medailles.total = int(donnees_medailles.gold_count) + int(donnees_medailles.silver_count) + int(donnees_medailles.bronze_count)

            db.session.commit()

            flash("La modification des données sur le pays " + nom_pays + " pour l'édition " + annee_participation + " s'est correctement déroulée", 'success')

    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de la modification des données sur le pays " + nom_pays + " pour l'année " + annee_participation + " : " + str(e), "error")
        db.session.rollback()

    return render_template("pages/edition_ajout.html", form=form, nom_pays=nom_pays, annee_participation=annee_participation, donnees_donnees=donnees_donnees, donnees_medailles=donnees_medailles)