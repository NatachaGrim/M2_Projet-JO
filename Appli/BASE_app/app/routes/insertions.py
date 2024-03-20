from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import InsertionUsers, AjoutAll
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
        donnees = [] # Initialiser données comme une liste vide

        if form.validate_on_submit():
            mail = clean_arg(request.form.get("mail", None))
            pseudo = clean_arg(request.form.get("pseudo", None))
            mot_de_passe = clean_arg(request.form.get("mot_de_passe", None))

            if mail and pseudo and mot_de_passe:
                    nouvel_utilisateur, erreurs = Users().Ajout(pseudo=pseudo, password=mot_de_passe, mail=mail) # Si l'on ne met pas ", erreurs" ici python considère que notre variable est égale à un tuple car notre méthode renvoie un tuple avec l'erreur et le contenu de la notre requête
                    print(nouvel_utilisateur)
                    if nouvel_utilisateur:
                        flash(f"L'utilisateur {nouvel_utilisateur.pseudo} a bien été ajouté dans la base.", 'success')
                    else:
                        flash(f"L'utilisateur n'a pas été ajouté dans la base. Erreurs : ", 'error')
        else:
            flash("Merci d'indiquer vos informations de création de compte.", 'info')
     
    except Exception as e:
            print("Une erreur est survenue : " + str(e))
            flash("Une erreur s'est produite lors de l'ajout de l'utilisateur, avez-vous respecté les contraintes de saisie ?" + str(e), 'info')
            db.session.rollback()
            abort(500)

    return render_template("pages/ajout_utilisateur.html", sous_titre="Recherche", donnees=donnees, form=form, nouvel_utilisateur=nouvel_utilisateur)

@app.route("/insertion/all", methods=['GET', 'POST'])
@login_required
def insertion_all():
    """
    Route permettant l'insertion de données pour un pays et une édition des Jeux Olympiques. Les 
    données déjà en base ne seront pas ajoutées

    L'utilisateur doit être connecté pour insérer des données via ce formulaire

    Parameters
    ----------
    None

    Returns
    -------
    template
        Retourne le même template ajout_all.html avec un message flash en fonction du déroulement 
        de l'ajout
    
    Raises
    ------
    500 Internal Server Error
        Si une erreur inattendue se produit lors du traitement du formulaire.
    """
    form = AjoutAll() # Récupération des données saisies dans le formulaire

    try:
        if form.validate_on_submit(): # Récupération de l'ensemble des données à ajouter en base
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

            clef_p = f"{code_pays} - {annee_participation}"
            
            # Vérification de l'existence des données en base
            pays_existant = Pays.query.filter_by(nom=nom_pays).first()

            # Ajout des données en base
            if not pays_existant:
                nouveau_pays = Pays(
                    noc=code_pays,
                    nom=nom_pays,
                    latitude=latitude_pays,
                    longitude=longitude_pays)
                db.session.add(nouveau_pays)

            # Vérification de l'existence des données en base
            annee_existante = Formulaire.query.filter_by(id_team=clef_p).first()

            # Ajout des données en base
            if not annee_existante:
                nouvelle_participation = Formulaire(
                    id_team=clef_p,
                    noc=code_pays,
                    year=annee_participation)
                
                nouvelles_donnees = Donnees(
                    id_team=clef_p,
                    population=population_pays,
                    richesse=richesse_pays,
                    investissement=investissement_pays)
                
                nouvelles_medailles = Medailles(
                    id_team=clef_p,
                    gold_count=int(gold),
                    silver_count=int(silver),
                    bronze_count=int(bronze),
                    total=int(gold)+int(silver)+int(bronze))
                        
                db.session.add(nouvelle_participation)
                db.session.add(nouvelles_donnees)
                db.session.add(nouvelles_medailles)

            else:
                flash("Les données pour le pays " + nom_pays + " pour l'année " + annee_participation + " sont déjà dans la base de données", 'warning')
            db.session.commit()
            flash("L'insertion des données sur le pays " + nom_pays + " pour l'année " + annee_participation + " s'est correctement déroulée", 'success')
        
        else:
            flash("Veuillez renseigner l'ensemble des champs pour insérer la participation", 'error')
    
    except Exception as e :
        print("Une erreur est survenue : " + str(e))
        flash("Une erreur s'est produite lors de l'insertion des données sur le pays " + nom_pays + " pour l'année " + annee_participation + " : " + str(e), "error")
        db.session.rollback()
        abort(500)
    
    return render_template("pages/ajout_all.html", sous_titre="Insertion données", form=form)
