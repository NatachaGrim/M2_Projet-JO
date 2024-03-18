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
    form.nom_pays.choices = [('','')] + [(pays.nom) for pays in Pays.query.all()]

    def delete_pays(pays):
        # vérifier que le pays existe bien en base
        pays = Pays.query.get(nom_pays)
        if pays:
            db.session.delete(pays)
            db.session.commit()

    try:
        if form.validate_on_submit():
            nom_pays =  clean_arg(request.form.get("nom_pays", None))

            if nom_pays:
                delete_pays(nom_pays)
                flash("La suppression du pays s'est correctement déroulée", 'info')
            
            else:
                flash("Le pays indiqué ne figure pas dans la base", "error")
    
    except Exception as e :
        flash("Une erreur s'est produite lors de la suppression : " + str(e), "error")
    
    return render_template("pages/suppression_pays.html", sous_titre= "Suppression pays", form=form)
