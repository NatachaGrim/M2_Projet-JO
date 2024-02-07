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
cd Application
```

- Puis collez-y la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
virtualenv env -p python3
```

### Étape 4 : télécharger la base de données
- Téléchargez la base de données et déplacez-la dans le dossier "Application".

### Étape 5 : saisir les variables
- Dans le terminal, collez la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
touch .env
```

- Ouvrez le fichier ```.env``` et copiez-collez-y ce bloc de code avec ```ctrl+v``` :

```
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
localhost:5000/nomDeRoute
```

Nos différentes routes sont consultables dans [ce dossier]().

## Étape 8 : quitter l'application
- Dans le terminal, maintenez la touche ```ctrl``` enfoncée et appuyez sur la touche ```c``` ;
- Collez-y ensuite la ligne suivante avec ```ctrl+maj+v``` et appuyez sur la touche ```Entrée``` :

```shell
deactivate
```

## Instructions : mémo

Pour lancer l'application :
```shell
cd cheminJusqu'auDossierApplication
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
