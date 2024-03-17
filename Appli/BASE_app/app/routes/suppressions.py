from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import SuppressionPays
from ..utils.transformations import clean_arg
from flask_login import current_user, logout_user, login_user, login_required
from .users import admin_required

@app.route("/suppression/pays", methods=['GET', 'POST'])
#@login_required
def suppression_pays():
    form = SuppressionPays()

    def delete_pays(noc):
        pays = Pays.query.get(noc)
        if pays:
            db.session.delete(pays)
            db.session.commit()

    try:
        if form.validate_on_submit():
            code_pays =  clean_arg(request.form.get("code_pays", None))

            if code_pays:
                delete_pays(code_pays)
                flash("La suppression du pays s'est correctement déroulée", 'success')
            
            else:
                flash("Le code ne correspond à aucun pays en base", "error")
    
    except Exception as e :
        flash("Une erreur s'est produite lors de la suppression : " + str(e), "error")
    
    return render_template("pages/suppression_pays.html", sous_titre= "Suppression pays", form=form)
