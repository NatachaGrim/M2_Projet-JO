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
Les variables sont indispensables au bon fonctionnement de l'application. Vous devrez les ajouter manuellement dans un fichier caché nommé ```.env```. Elles sont indiquées ci-dessous.

## Instructions : un premier lancement

### Étape 1 : installer Python
- Ouvrez votre terminal, collez-y la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
sudo apt install python3
```

### Étape 2 : cloner l'application
- Dans le terminal, collez la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
git clone https://github.com/NatachaGrim/M2_Projet-JO.git
```

### Étape 3 : installer un environnement virtuel
- Dans le terminal, collez la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
cd Appli/BASE_app
```

- Puis collez-y la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
virtualenv env -p python3
```

### Étape 4 : télécharger la base de données
- Téléchargez la base de données et déplacez-la dans le dossier ```Appli```.

### Étape 5 : saisir les variables
- Dans le terminal, collez la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
touch .env
```

- Ouvrez le fichier ```.env``` et copiez-collez-y ce bloc de code avec ```ctrl+v``` :

```shell
DEBUG=False
SQLALCHEMY_DATABASE_URI= [URI DE LA BASE SQLITE]
PAYS_PER_PAGE = 10 
RESOURCES_PER_PAGE = 20
SQLALCHEMY_ECHO=False
WTF_CSRF_ENABLE=True
SECRET_KEY=[LA CLÉ SERA ENVOYÉE PAR MAIL]
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587	
MAIL_USERNAME=[LE NOM SERA ENVOYÉ PAR MAIL]
SECRET_KEY=[LA CLÉ SECRÈTE SERA ENVOYÉE PAR MAIL]
MAIL_USE_TLS=True
MAIL_DEFAULT_SENDER=maxime.griveau@chartes.psl.eu
```

- Enregistrez avec ```ctrl+s``` et fermez le fichier.

## Étape 6 : installer les dépendances
- Dans le terminal, collez la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
source env/bin/activate
```

- Collez ensuite la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
pip install -r requirements.txt
```

## Étape 7 : lancer l'application

- Dans le terminal, collez la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
python run.py
```

L'application devrait démarrer. Ouvrez ensuite votre navigateur web et saisissez le nom d'une route. Par exemple :

```shell
localhost:5000/accueil
```

Nos différentes routes sont consultables dans [ce dossier](Appli/BASE_app/app/routes).

## Étape 8 : quitter l'application
- Dans le terminal, maintenez la touche ```ctrl``` enfoncée et appuyez sur la touche ```c``` ;
- Collez-y ensuite la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
deactivate
```

## Instructions : mémo

Pour lancer l'application :
```shell
cd cheminJusqu'auDossierBASE_app
```

```shell
source env/bin/activate
```

```shell
python run.py
```

Pour quitter l'application :
- Maintenir ```ctrl``` et appuyer sur ```c``` ;

```shell
deactivate
```
