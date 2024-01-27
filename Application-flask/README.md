# Application flask
Notre application permet de consulter les résultats de différents pays à diverses éditions des Jeux Olympiques.

## Contributeurs
Les personnes ayant contribué sont :
- [Théo Burnel](https://github.com/TheoBurnel) ;
- [Natacha Grim](https://github.com/NatachaGrim) ;
- [Maxime Griveau](https://github.com/Maxime-Griveau) ;
- [Mohammed Mechentel]().

## Fonctionnalités
Notre application dispose des fonctionnalités suivantes :

## Variables
Les variables sont indispensables au bon fonctionnement de l'application. Vous devrez les ajouter manuellement dans un fichier. Copiez-collez simplement ce bloc de texte :

## Instructions : un premier lancement

### Étape 1 : installer Python
- Ouvrez votre terminal et saisissez : ```sudo apt install python3```.

### Étape 2 : cloner l'application
- En haut [de cette page](https://github.com/NatachaGrim/M2_Projet-JO), cliquez sur le bouton vert "Code" ;
- Copiez le lien HTTPS ;
- Dans le terminal, saisissez ```git clone``` et collez le lien (ctrl+maj+v).

### Étape 3 : installer un environnement virtuel
- Positionnez-vous dans le dossier de l'application grâce à la commande ```cd Application``` ;
- Installez un environnement virutel avec la commande ```virtualenv env -p python3```.

### Étape 4 : télécharger la base de données
- Téléchargez la base de données et déplacez-la dans le dossier "Application".

### Étape 5 : saisir les variables
- Dans le terminal, saisissez ```touch .env``` ;
- Ouvrez le fichier ```.env``` et copiez-collez les variables indiquées [ci-dessus](https://github.com/NatachaGrim/M2_Projet-JO/tree/main/Application-flask#variables).

## Étape 6 : installer les dépendances
- Dans le terminal, saisissez ```source env/bin/activate``` ;
- Saisissez ensuite ```pip install -r requirements.txt```.

## Étape 7 : lancer l'application
- Saisissez ```python run.py```, l'application devrait démarrer ;
- Ouvrez votre navigateur web ;
- Saisissez une route dans la barre d'URL : ```localhost:5000/nomDeRoute```.

Nos différentes routes sont consultables dans [ce dossier]().

## Étape 8 : quitter l'application
- Maintenez la touche ```ctrl``` enfoncée dans votre terminal et appuyez sur la touche ```c``` ;
- Saisissez ```deactivate```.

## Instructions : mémo

Pour lancer l'application :
- ```cd cheminJusqu'auDossierApplication``` ;
- ```source env/bin/activate``` ;
- ```python run.py```.

Pour quitter l'application :
- ```ctrl+c``` ;
- ```deactivate```.
