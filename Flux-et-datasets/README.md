# À propos

Ce dossier contient les deux flux de traitement de la donnée, réalisés avec le logiciel Dataiku, ainsi que les fichiers csv de sortie.

## Flux sur les médailles et les investissements

Nous avons travaillé sur le nombre de médailles remportées à six éditions des Jeux Olympiques (1996, 2000, 2004, 2008, 2012, 2016) par les pays, mis en relief avec le PIB des pays et le pourcentage de ce dernier investi dans le domaine sportif.

Notre [flux](Medals-Pop-GDP/Flux-Medals-Pop-GDP.zip) a, à terme, généré un unique [fichier csv](Medals-Pop-GDP/Dataset-Medals-Pop-GDP.csv) de sortie.

## Flux comparant la France et le Royaume-Uni en natation

Sur la même période de temps, nous avons souhaité comparer la réussite de la France et du Royaume-Uni aux épreuves de natation, en fonction des médailles remportées et du nombre d'infrastructures sportives relatives par région et pour 100.000 habitants.

Ce [flux](Medals-Swim-France-England/Flux-Medals-Swim-France-England.zip) est composé de quatre mini-flux, lesquels ont chacun produit un fichier csv de sortie :
- [Médailles remportées par la France](Medals-Swim-France-England/Dataset-France-Medals-Swim.csv) ;
- [Nombre d'infrastructures pour 100.000 habitants en France](Medals-Swim-France-England/Dataset-France-Swimming-Pools-Per-100k-Inhabs.csv) ;
- [Médailles remportées par le Royaume-Uni](Medals-Swim-France-England/Dataset-England-Medals-Swim.csv) ;
- [Nombre d'infrastructures pour 100.000 habitants au Royaume-Uni](Medals-Swim-France-England/Dataset-England-Swimming-Pools-Per-100k-Inhabs.csv).
