# Requête SPARQL

Enrichissement obligatoire de nos données avec Wikidata _via_ une requête SPARQL. La présente requête affiche le nombre de la population de pays sur trente ans (1993 - 2023). Pour plus de détails, consulter le [journal de bord](Journal-de-bord/Journal-de-bord.pdf).

Pour tester la requête : [Wikidata : Service des requêtes SPARQL](https://query.wikidata.org/).

```sparql
SELECT ?paysLabel ?population ?date ?cio
WHERE 
{
  ?pays wdt:P31 wd:Q6256. # liste de tous les pays 
  ?pays wdt:P984 ?cio. #liste des codes CIO
  ?pays p:P1082 ?populationStatement. # déclaration de population
  ?populationStatement ps:P1082 ?population. # population 
  ?populationStatement pq:P585 ?date. # date
  FILTER(YEAR(?date) >= (YEAR(NOW()) - 30)). # filtre sur les trente dernières années
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }
           }
ORDER BY ?paysLabel ?date
```
