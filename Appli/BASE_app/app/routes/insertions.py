from ..app import app, db
from flask import render_template, request, flash, abort, redirect, url_for
from ..models.Jeux_Olympiques import Pays, Donnees, Medailles, Formulaire
from ..models.formulaires import InsertionUsers
from ..utils.transformations import clean_arg
from ..models.users import Users
from .courriel import envoyer_courriel # import de la fonction d'envoi de courriels : à chaque MAJ de la base les notifications seront envoyées 



@app.route("/insertion/utilisateur", methods=['GET', 'POST'])
def insertion_utilisateur():
    
    form = InsertionUsers()
    nouvel_utilisateur = ""
    try:
        donnees = [] # Initialiser données comme une liste vide

        if form.validate_on_submit():
            
            mail = clean_arg(request.form.get("mail", None))
            pseudo = clean_arg(request.form.get("pseudo", None))
            mot_de_passe = clean_arg(request.form.get("mot_de_passe", None))

            if mail and pseudo and mot_de_passe: 
                
                    # Assurez-vous que la méthode Ajout renvoie correctement l'utilisateur et les erreurs
                    nouvel_utilisateur, erreurs = Users().Ajout(pseudo=pseudo, password=mot_de_passe, mail=mail) #si on ne met pas ", erreurs" ici python considère que notre variable est égale à un tuple car notre méthode renvoie un tuple avec l'erreur et le contenu de la notre requête
                  
                    if nouvel_utilisateur:
                        flash(f"L'utilisateur {nouvel_utilisateur.pseudo} a bien été ajouté dans la base.", 'success')



                        #A SUPPRIMER PLUS TARD QUAND LA ROUTE D'INSERTION SERA AJOUTÉE À LA BASE ! 
                        envoyer_courriel()  # Appel de la fonction d'envoi de courriel
                        #C'EST IMPORTANT SINON ON VA SE FAIRE SPAM

                        #VRAIMENT PITIÉ
                        
                        return redirect(url_for("connexion"))
                    
                    else:
                        flash(f"L'utilisateur n'a pas été ajouté dans la base. Erreurs : ", 'error')
        else:
            flash("Merci d'indiquer vos informations de création de compte.", 'info')
     
    
    except Exception as e:
            print("Une erreur est survenue : " + str(e))  # Ça c'est l'erreur qui s'affichera dans les logs (back office)
            flash("Une erreur s'est produite lors de l'ajout de l'utilisateur, avez-vous respecté les contraintes de saisie ?" + str(e), 'info')
            db.session.rollback()  # On fait un rollback pour éviter de lock la base
          

    return render_template("pages/ajout_utilisateur.html", sous_titre="Recherche", donnees=donnees, form=form, nouvel_utilisateur=nouvel_utilisateur)
