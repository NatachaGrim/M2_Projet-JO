from ..app import app, db
from flask import render_template, request, flash, redirect, url_for
from sqlalchemy import or_
from ..models.Jeux_Olympiques import Pays, Donnees, Formulaire, Medailles
from flask_login import LoginManager, login_required
from .users import admin_required #import du décorateur admin requiered 



"""
    Route pour récupérer les données des formulaires soumis pour une année donnée.

    Méthodes acceptées
    ------------------
    GET, POST

    Parameters
    ----------
    annee : int, optional
        L'année pour laquelle récupérer les données. Par défaut, définie sur 1996.

    Returns
    -------
    template
        Retourne le template de la page de données avec les données nécessaires pour l'année sélectionnée et une liste des années disponibles.
"""
@app.route("/")
@app.route("/accueil")
def accueil():
    return render_template("pages/accueil.html")

@app.route('/donnees', methods=['GET', 'POST'])
@login_required
@admin_required 

def donnees():
    choix_annee = request.form.get('annee', default=1996, type=int)
    data = db.session.query(
        Formulaire.year, 
        Medailles.total, 
        Donnees.population, 
        Donnees.investissement, 
        Donnees.richesse,
        Pays.nom) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .filter(Formulaire.year == choix_annee) \
            .group_by(Donnees.id_team, Formulaire.year, Medailles.total, Donnees.population, Donnees.investissement, Donnees.richesse).all()

    annees = db.session.query(Formulaire.year.distinct()).order_by(Formulaire.year).all()

    return render_template("pages/donnees.html", donnees=data, annees=annees, annee_actuelle=choix_annee)

"""
    Route pour récupérer des données spécifiques sur un pays donné.

    Méthodes acceptées
    ------------------
    GET

    Parameters
    ----------
    nom_pays : str
        Le nom du pays pour lequel récupérer les données.

    Returns
    -------
    template
        Retourne le template de la page de données par pays avec les données nécessaires pour le pays spécifié.
"""


@app.route("/donnees_pays/<nom_pays>")
def donnees_pays(nom_pays):
    
    donnees_du_pays = db.session.query(
        Formulaire.year, 
        Medailles.total,
        Medailles.gold_count,
        Medailles.silver_count,
        Medailles.bronze_count, 
        Donnees.population, 
        Donnees.investissement, 
        Donnees.richesse,
        Pays.nom) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .filter(Pays.nom.ilike(f"%{nom_pays}%")).all()


    return render_template("pages/donnees_pays.html", nom_pays=nom_pays, donnees=donnees_du_pays)
"""
    Route pour effectuer une recherche rapide sur le nom des pays et récupérer les résultats paginés.

    Méthodes acceptées
    ------------------
    GET

    Parameters
    ----------
    chaine : str, optional
        La chaîne de recherche pour filtrer les résultats des pays.

    Returns
    -------
    template
        Retourne le template des résultats de recherche avec les données paginées correspondant à la chaîne de recherche fournie.
"""


@app.route("/recherche_rapide")
@app.route("/recherche_rapide/<int:page>")
def recherche_rapide(page=1):
    chaine = request.args.get("chaine", None)
    resultats = None
    
    if chaine:
        # Utilisation de la fonction filter() pour filtrer les résultats en fonction de la chaîne de recherche
        donnees = db.session.query(
            Formulaire.year, 
            Pays.nom
        ).join(Pays, Pays.noc == Formulaire.noc) \
         .filter(
             #notre recherche_rapide ne portera que sur le nom du pays car il nous a semblé que c'est la seule chose qu'on pourrait vouloir chercher dans notre base
             Pays.nom.ilike(f"%{chaine}%")
         ).group_by(
            Formulaire.year, Pays.nom
         ).paginate(page=page, per_page=10)  # Pagination: 10 résultats par page
    else:
        # Si aucune chaîne de recherche n'est fournie, retournez None
        donnees = None
        
    return render_template(
        "pages/resultats_recherche.html", 
        sous_titre="Recherche | " + chaine if chaine else "Recherche rapide",
        donnees=donnees,
        requete=chaine
    )
