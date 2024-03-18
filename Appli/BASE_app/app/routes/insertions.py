from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import InsertionUsers, AjoutPays, AjoutParticipation, AjoutDonnees, AjoutMedailles, AjoutAll
from ..utils.transformations import clean_arg
from flask_login import current_user, logout_user, login_user, login_required
from ..models.users import Users
from .users import admin_required

@app.route("/insertion/utilisateur", methods=['GET', 'POST'])
@app.route("/insertion_utilisateur/<int:page>", methods=['GET', 'POST'])
def insertion_utilisateur(page=1):
    
    form = InsertionUsers()
    nouvel_utilisateur = ""
    try:
        donnees = [] # Initialisation de données comme une liste vide

        if form.validate_on_submit():
            
            mail = clean_arg(request.form.get("mail", None))
            pseudo = clean_arg(request.form.get("pseudo", None))
            mot_de_passe = clean_arg(request.form.get("mot_de_passe", None))

            if mail and pseudo and mot_de_passe: 
                
                    
                    nouvel_utilisateur, erreurs = Users().Ajout(pseudo=pseudo, password=mot_de_passe, mail=mail) #si on ne met pas ", erreurs" ici python considère que notre variable est égale à un tuple car notre méthode renvoie un tuple avec l'erreur et le contenu de la notre requête
                    print(nouvel_utilisateur)
                    if nouvel_utilisateur:
                        flash(f"L'utilisateur {nouvel_utilisateur.pseudo} a bien été ajouté dans la base.", 'success')
                    else:
                        flash(f"L'utilisateur n'a pas été ajouté dans la base. Erreurs : ", 'error')
        else:
            flash("Merci d'indiquer vos informations de création de compte.", 'info')
     
    
    except Exception as e:
            print("Une erreur est survenue : " + str(e))  # Ça c'est l'erreur qui s'affichera dans les logs (back office)
            flash("Une erreur s'est produite lors de l'ajout de l'utilisateur, avez-vous respecté les contraintes de saisie ?" + str(e), 'info')
            db.session.rollback()  # On fait un rollback pour éviter de lock la base
          

    return render_template("pages/ajout_utilisateur.html", sous_titre="Recherche", donnees=donnees, form=form, nouvel_utilisateur=nouvel_utilisateur)
    




@app.route("/insertion/pays", methods=['GET', 'POST'])
#@login_required
def insertion_pays():
    form = AjoutPays()

    try:
        if form.validate_on_submit():
            code_pays = clean_arg(request.form.get("code_pays", None))
            nom_pays = clean_arg(request.form.get("nom_pays", None))
            latitude_pays = clean_arg(request.form.get("latitude_pays", None))
            longitude_pays = clean_arg(request.form.get("longitude_pays", None))

            nouveau_pays = Pays(
                noc=code_pays,
                nom=nom_pays,
                latitude=latitude_pays,
                longitude=longitude_pays)

            db.session.add(nouveau_pays)
            db.session.commit()

            flash("L'insertion du pays " + nom_pays + " s'est correctement déroulée", 'success')
        else:
            flash("Veuillez renseigner l'ensemble des champs obligatoires", 'error')
    
    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'insertion du pays " + nom_pays + " : " + str(e), "error")
        db.session.rollback()
    
    return render_template("pages/ajout_pays.html", sous_titre="Insertion pays", form=form)





@app.route("/insertion/participation", methods=['GET', 'POST'])
#@login_required
def insertion_participation():
    form = AjoutParticipation()

    try:
        if form.validate_on_submit():
            code_pays = clean_arg(request.form.get("code_pays", None))
            annee_participation = clean_arg(request.form.get("annee_participation", None))

            nouvelle_participation = Formulaire(
                id_team=f"{code_pays} - {annee_participation}",
                noc=code_pays,
                year=annee_participation) 

            db.session.add(nouvelle_participation)
            db.session.commit()

            flash("L'insertion de la participation du pays " + code_pays + " l'année " + annee_participation + " s'est correctement déroulée", 'success')
        else:
            flash("Veuillez renseigner l'ensemble des champs obligatoires", 'error')
    
    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'insertion du pays " + code_pays + " l'année " + annee_participation + " : " + str(e), "error")
        db.session.rollback()
    
    return render_template("pages/ajout_participation.html", sous_titre="Insertion participation", form=form)





@app.route("/insertion/donnees", methods=['GET', 'POST'])
#@login_required
def insertion_donnees():
    form = AjoutDonnees()

    try:
        if form.validate_on_submit():
            code_pays = clean_arg(request.form.get("code_pays", None))
            annee_participation = clean_arg(request.form.get("annee_participation", None))
            population_pays = clean_arg(request.form.get("population_pays", None))
            richesse_pays = clean_arg(request.form.get("richesse_pays", None))
            investissement_pays = clean_arg(request.form.get("investissement_pays", None))

            nouvelles_donnees = Donnees(
                id_team=f"{code_pays} - {annee_participation}",
                population=population_pays,
                richesse=richesse_pays,
                investissement=investissement_pays)

            db.session.add(nouvelles_donnees)
            db.session.commit()

            flash("L'insertion des données sur le pays " + code_pays + " pour l'année " + annee_participation + " s'est correctement déroulée", 'success')
        else:
            flash("Veuillez renseigner l'ensemble des champs obligatoires", 'error')
    
    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'insertion des données sur le pays " + code_pays + " pour l'année " + annee_participation + " : " + str(e), "error")
        db.session.rollback()
    
    return render_template("pages/ajout_donnees.html", sous_titre="Insertion données", form=form)





@app.route("/insertion/medailles", methods=['GET', 'POST'])
#@login_required
def insertion_medailles():
    form = AjoutMedailles()

    try:
        if form.validate_on_submit():
            code_pays = clean_arg(request.form.get("code_pays", None))
            annee_participation = clean_arg(request.form.get("annee_participation", None))
            gold = clean_arg(request.form.get("gold", None))
            silver = clean_arg(request.form.get("silver", None))
            bronze = clean_arg(request.form.get("bronze", None))

            nouvelles_medailles = Medailles(
                id_team=f"{code_pays} - {annee_participation}",
                gold_count=gold,
                silver_count=silver,
                bronze_count=bronze,
                total=gold+silver+bronze)

            db.session.add(nouvelles_medailles)
            db.session.commit()

            flash("L'insertion des médailles remportées par le pays " + code_pays + " pour l'année " + annee_participation + " s'est correctement déroulée", 'success')
        else:
            flash("Veuillez renseigner l'ensemble des champs pour insérer la participation", 'error')
    
    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'insertion des médailles remportées par le pays " + code_pays + " pour l'année " + annee_participation + " : " + str(e), "error")
        db.session.rollback()
    
    return render_template("pages/ajout_medailles.html", sous_titre="Insertion médailles", form=form)





@app.route("/insertion/all", methods=['GET', 'POST'])
#@login_required
def insertion_all():
    form = AjoutAll()

    try:
        if form.validate_on_submit():
            code_pays = clean_arg(request.form.get("code_pays", None))
            nom_pays = clean_arg(request.form.get("nom_pays", None))
            latitude_pays = clean_arg(request.form.get("latitude_pays", None))
            longitude_pays = clean_arg(request.form.get("longitude_pays", None))
            annee_participation = clean_arg(request.form.get("annee_participation", None))
            population_pays = clean_arg(request.form.get("population_pays", None))
            richesse_pays = clean_arg(request.form.get("richesse_pays", None))
            investissement_pays = clean_arg(request.form.get("investissement_pays", None))
            gold = clean_arg(request.form.get("gold", None))
            silver = clean_arg(request.form.get("silver", None))
            bronze = clean_arg(request.form.get("bronze", None))
            
            print("ok1")

            nouveau_pays = Pays(
                noc=code_pays,
                nom=nom_pays,
                latitude=latitude_pays,
                longitude=longitude_pays)

            print("ok2")

            nouvelle_participation = Formulaire(
                id_team=f"{code_pays} - {annee_participation}",
                noc=code_pays,
                year=annee_participation)
            
            print("ok3")

            nouvelles_donnees = Donnees(
                id_team=f"{code_pays} - {annee_participation}",
                population=population_pays,
                richesse=richesse_pays,
                investissement=investissement_pays)
            
            print("ok4")

            nouvelles_medailles = Medailles(
                id_team=f"{code_pays} - {annee_participation}",
                gold_count=gold,
                silver_count=silver,
                bronze_count=bronze,
                total=gold+silver+bronze)
            
            print("ok5")

            db.session.add(nouveau_pays)

            print("ok6")
            
            db.session.add(nouvelle_participation)

            print("ok7")

            db.session.add(nouvelles_donnees)

            print("ok8")

            db.session.add(nouvelles_medailles)

            print("ok9")
         
            db.session.commit()

            print("ok10")

            flash("L'insertion des données sur le pays " + nom_pays + " pour l'année " + annee_participation + " s'est correctement déroulée", 'success')
        else:
            flash("Veuillez renseigner l'ensemble des champs pour insérer la participation", 'error')
    
    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'insertion des données sur le pays " + nom_pays + " pour l'année " + annee_participation + " : " + str(e), "error")
        db.session.rollback()
    
    return render_template("pages/ajout_all.html", sous_titre="Insertion données", form=form)


