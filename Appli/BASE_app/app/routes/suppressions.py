from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import SuppressionPays
from ..utils.transformations import clean_arg
from flask_login import current_user, logout_user, login_user, login_required
from ..models.users import Users
from .users import admin_required

@app.route("/suppression/pays", methods=['GET', 'POST'])
@login_required
def suppression_pays():
    form = SuppressionPays()

    liste_pays = Pays.query.all()    
    form.nom_pays.choices = [('')] + [(p.nom) for p in liste_pays]

    try:
        if form.validate_on_submit():
            nom_pays =  clean_arg(request.form.get("nom_pays", None))
            annee_participation = clean_arg(request.form.get("annee_participation", None))

            donnees_pays = Pays.query.filter_by(nom=nom_pays).first()
            code_pays = donnees_pays.noc
            clef_p=f"{code_pays} - {annee_participation}"

            donnees_formulaire = Formulaire.query.filter_by(id_team=clef_p).first()
            donnees_donnees = Donnees.query.filter_by(id_team=clef_p).first()
            donnees_medailles = Medailles.query.filter_by(id_team=clef_p).first()

            if donnees_pays:
                db.session.delete(donnees_pays)
            
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
    
    return render_template("pages/suppression_pays.html", sous_titre="Suppression pays", form=form)