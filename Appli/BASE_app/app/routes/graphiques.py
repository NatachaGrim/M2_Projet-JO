from flask import render_template, jsonify, request
from ..app import app, db
from ..models.Jeux_Olympiques import Pays, Donnees, Formulaire, Medailles
import json


@app.route("/visualisation")
def visualisation():
    return render_template("pages/visualisation.html")

@app.route("/carte")
def carte():
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

    # Conversion des données en JSON et écriture dans un fichier
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
        
        with open('./app/statics/data/donnees.js', 'w') as f:
            f.write('var geojson_RAMA = ')
            json.dump({"features": data_json}, f)

    return render_template("pages/graph/carte.html")



#Seconde route vers les visualisations. Ici, on crée aussi un jeu pour chaque année.
#Les jeux sont mis à jour et générés à chaque lancement de la route.
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

    # Conversion des données en un format compatible avec Chart.js
    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    # Écriture des données dans un fichier JSON
    with open('./app/statics/data/donnees_1996.json', 'w') as f:
        json.dump(data_json, f)

    annees = db.session.query(Formulaire.year.distinct()).order_by(Formulaire.year).all()
    
    return render_template("pages/graph/graphiques_1996.html")

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

    # Conversion des données en un format compatible avec Chart.js
    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    # Écriture des données dans un fichier JSON
    with open('./app/statics/data/donnees_2000.json', 'w') as f:
        json.dump(data_json, f)

    annees = db.session.query(Formulaire.year.distinct()).order_by(Formulaire.year).all()
    
    return render_template("pages/graph/graphiques_2000.html")

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

    # Conversion des données en un format compatible avec Chart.js
    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    # Écriture des données dans un fichier JSON
    with open('./app/statics/data/donnees_2004.json', 'w') as f:
        json.dump(data_json, f)

    annees = db.session.query(Formulaire.year.distinct()).order_by(Formulaire.year).all()
    
    return render_template("pages/graph/graphiques_2004.html")

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

    # Conversion des données en un format compatible avec Chart.js
    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    # Écriture des données dans un fichier JSON
    with open('./app/statics/data/donnees_2008.json', 'w') as f:
        json.dump(data_json, f)

    return render_template("pages/graph/graphiques_2008.html")

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

    # Conversion des données en un format compatible avec Chart.js
    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    # Écriture des données dans un fichier JSON
    with open('./app/statics/data/donnees_2012.json', 'w') as f:
        json.dump(data_json, f)

    return render_template("pages/graph/graphiques_2012.html")

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

    # Conversion des données en un format compatible avec Chart.js
    data_json = []
    for donnee in data:
        valeurs = {
            "pays": donnee.nom,
            "medailles": donnee.total,
            "population": donnee.population,
            "richesse": donnee.richesse,
        }
        data_json.append(valeurs)

    # Écriture des données dans un fichier JSON
    with open('./app/statics/data/donnees_2016.json', 'w') as f:
        json.dump(data_json, f)

    return render_template("pages/graph/graphiques_2016.html")
