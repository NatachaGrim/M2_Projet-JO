from flask import render_template, jsonify
from ..app import app, db
from ..models.Jeux_Olympiques import Pays, Donnees, Formulaire, Medailles
import json

@app.route("/graphiques")
def graphiques():
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

    return render_template("pages/graphiques.html")
