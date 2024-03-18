from flask import render_template, jsonify, request
from ..app import app, db
from ..models.Jeux_Olympiques import Pays, Donnees, Formulaire, Medailles
import json


@app.route("/visualisation")
def visualisation():
    return render_template("pages/visualisation.html")
    """
    Route pour afficher la page de visualisation.

    Returns
    -------
    template
        Retourne le template visualisation.html
    """

@app.route("/carte")
def carte():        
    
    # Requête pour récupérer les données nécessaires à la visualisation
    data = db.session.query(
        Formulaire.year, 
        Medailles.total,
        Donnees.population, 
        Donnees.investissement, 
        Donnees.richesse,
        Pays.nom,
        Pays.latitude,
        Pays.longitude) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .group_by(Donnees.id_team, Formulaire.year, Medailles.total, Donnees.population, Donnees.investissement, Donnees.richesse).all()

    # Convertir les données en format JSON pour la carte
    data_json = []
    for donnee in data:
        coordinates = [donnee.longitude, donnee.latitude]
        properties = {
            "Pays": donnee.nom,
            "Annees": donnee.year,
            "Médailles": donnee.total,
            "Population": donnee.population,
            "Richesse": donnee.richesse,
            "Investissements": donnee.investissement
        }
        feature = {
            "geometry": {"coordinates": coordinates, "type": "Point"},
            "properties": properties,
            "type": "Feature"
        }
        data_json.append(feature)

        # Écrire les données JSON dans un fichier
        with open('./app/statics/data/donnees.js', 'w') as f:
            f.write('var geojson_RAMA = ')
            json.dump({"features": data_json}, f)
 
    # Rendre le template carte.html avec les données JSON
    return render_template("pages/graph/carte.html")
    """
    Route pour générer la carte avec les données de visualisation.

    Returns
    -------
    template
        Retourne le template carte.html
    """


@app.route('/graphiques_1996', methods=['GET', 'POST'])
def graphiques_1996():
    choix_annee = 1996
    data = db.session.query(
        Formulaire.year, 
        Medailles.total, 
        Donnees.population, 
        Donnees.richesse,
        Pays.nom) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .filter(Formulaire.year == choix_annee) \
            .group_by(Donnees.id_team, Formulaire.year, Medailles.total, Donnees.population, Donnees.richesse).all()

    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    with open('./app/statics/data/donnees_1996.json', 'w') as f:
        json.dump(data_json, f)

    annees = db.session.query(Formulaire.year.distinct()).order_by(Formulaire.year).all()
    
    return render_template("pages/graph/graphiques_1996.html")
    """
    Route pour afficher les graphiques pour l'année 1996.

    Cette route récupère les données nécessaires à partir de la base de données pour générer des graphiques représentant diverses statistiques pour l'année 1996. Ces données comprennent le total des médailles remportées par chaque pays, la population de chaque pays, ainsi que la richesse mesurée de chaque pays. Ces données sont ensuite converties en format JSON pour être utilisées dans les graphiques.

    Returns
    -------
    template
        Retourne le template graphiques_1996.html, qui contient les graphiques générés à partir des données récupérées.
    """

@app.route('/graphiques_2000', methods=['GET', 'POST'])
def graphiques_2000():
    choix_annee = 2000
    data = db.session.query(
        Formulaire.year, 
        Medailles.total, 
        Donnees.population, 
        Donnees.richesse,
        Pays.nom) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .filter(Formulaire.year == choix_annee) \
            .group_by(Donnees.id_team, Formulaire.year, Medailles.total, Donnees.population, Donnees.richesse).all()

    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    with open('./app/statics/data/donnees_2000.json', 'w') as f:
        json.dump(data_json, f)

    annees = db.session.query(Formulaire.year.distinct()).order_by(Formulaire.year).all()
    
    return render_template("pages/graph/graphiques_2000.html")
    """
    Route pour afficher les graphiques pour l'année 2000.

    Cette route récupère les données nécessaires à partir de la base de données pour générer des graphiques représentant diverses statistiques pour l'année 2000. Ces données comprennent le total des médailles remportées par chaque pays, la population de chaque pays, ainsi que la richesse mesurée de chaque pays. Ces données sont ensuite converties en format JSON pour être utilisées dans les graphiques.

    Returns
    -------
    template
        Retourne le template graphiques_2000.html, qui contient les graphiques générés à partir des données récupérées.
    """

@app.route('/graphiques_2004', methods=['GET', 'POST'])
def graphiques_2004():
    choix_annee = 2004
    data = db.session.query(
        Formulaire.year, 
        Medailles.total, 
        Donnees.population, 
        Donnees.richesse,
        Pays.nom) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .filter(Formulaire.year == choix_annee) \
            .group_by(Donnees.id_team, Formulaire.year, Medailles.total, Donnees.population, Donnees.richesse).all()

    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    with open('./app/statics/data/donnees_2004.json', 'w') as f:
        json.dump(data_json, f)

    annees = db.session.query(Formulaire.year.distinct()).order_by(Formulaire.year).all()
    
    return render_template("pages/graph/graphiques_2004.html")
    """
    Route pour afficher les graphiques pour l'année 2004.

    Cette route récupère les données nécessaires à partir de la base de données pour générer des graphiques représentant diverses statistiques pour l'année 2000. Ces données comprennent le total des médailles remportées par chaque pays, la population de chaque pays, ainsi que la richesse mesurée de chaque pays. Ces données sont ensuite converties en format JSON pour être utilisées dans les graphiques.

    Returns
    -------
    template
        Retourne le template graphiques_2004.html, qui contient les graphiques générés à partir des données récupérées.
    """

@app.route('/graphiques_2008', methods=['GET', 'POST'])
def graphiques_2008():
    choix_annee = 2008
    data = db.session.query(
        Formulaire.year, 
        Medailles.total, 
        Donnees.population, 
        Donnees.richesse,
        Pays.nom) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .filter(Formulaire.year == choix_annee) \
            .group_by(Donnees.id_team, Formulaire.year, Medailles.total, Donnees.population, Donnees.richesse).all()

    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    with open('./app/statics/data/donnees_2008.json', 'w') as f:
        json.dump(data_json, f)

    return render_template("pages/graph/graphiques_2008.html")
    """
    Route pour afficher les graphiques pour l'année 2008.

    Cette route récupère les données nécessaires à partir de la base de données pour générer des graphiques représentant diverses statistiques pour l'année 2000. Ces données comprennent le total des médailles remportées par chaque pays, la population de chaque pays, ainsi que la richesse mesurée de chaque pays. Ces données sont ensuite converties en format JSON pour être utilisées dans les graphiques.

    Returns
    -------
    template
        Retourne le template graphiques_2008.html, qui contient les graphiques générés à partir des données récupérées.
    """

@app.route('/graphiques_2012', methods=['GET', 'POST'])
def graphiques_2012():
    choix_annee = 2012
    data = db.session.query(
        Formulaire.year, 
        Medailles.total, 
        Donnees.population, 
        Donnees.richesse,
        Pays.nom) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .filter(Formulaire.year == choix_annee) \
            .group_by(Donnees.id_team, Formulaire.year, Medailles.total, Donnees.population, Donnees.richesse).all()

    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    with open('./app/statics/data/donnees_2012.json', 'w') as f:
        json.dump(data_json, f)

    return render_template("pages/graph/graphiques_2012.html")
    """
    Route pour afficher les graphiques pour l'année 2012.

    Cette route récupère les données nécessaires à partir de la base de données pour générer des graphiques représentant diverses statistiques pour l'année 2000. Ces données comprennent le total des médailles remportées par chaque pays, la population de chaque pays, ainsi que la richesse mesurée de chaque pays. Ces données sont ensuite converties en format JSON pour être utilisées dans les graphiques.

    Returns
    -------
    template
        Retourne le template graphiques_2012.html, qui contient les graphiques générés à partir des données récupérées.
    """

@app.route('/graphiques_2016', methods=['GET', 'POST'])
def graphiques_2016():
    choix_annee = 2016
    data = db.session.query(
        Formulaire.year, 
        Medailles.total, 
        Donnees.population, 
        Donnees.richesse,
        Pays.nom) \
            .join(Donnees, Formulaire.id_team == Donnees.id_team) \
            .join(Medailles, Medailles.id_team == Donnees.id_team) \
            .join(Pays, Pays.noc == Formulaire.noc) \
            .filter(Formulaire.year == choix_annee) \
            .group_by(Donnees.id_team, Formulaire.year, Medailles.total, Donnees.population, Donnees.richesse).all()

    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    with open('./app/statics/data/donnees_2016.json', 'w') as f:
        json.dump(data_json, f)

    return render_template("pages/graph/graphiques_2016.html")
    """
    Route pour afficher les graphiques pour l'année 2016.

    Cette route récupère les données nécessaires à partir de la base de données pour générer des graphiques représentant diverses statistiques pour l'année 2000. Ces données comprennent le total des médailles remportées par chaque pays, la population de chaque pays, ainsi que la richesse mesurée de chaque pays. Ces données sont ensuite converties en format JSON pour être utilisées dans les graphiques.

    Returns
    -------
    template
        Retourne le template graphiques_2016.html, qui contient les graphiques générés à partir des données récupérées.
    """