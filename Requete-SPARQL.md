# Requête SPARQL

Enrichissement obligatoire de nos données avec Wikidata _via_ une requête SPARQL. La présente requête affiche le nombre de la population de pays sur trente ans (1993 - 2023).

```sparql
SELECT ?paysLabel ?population ?date
WHERE
{
  ?pays wdt:P31 wd:Q6256.
  ?pays p:P1082 ?populationStatement.
  ?populationStatement ps:P1082 ?population.
  ?populationStatement pq:P585 ?date.
  
  FILTER(YEAR(?date) >= (YEAR(NOW()) - 30)).
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }
           }
ORDER BY ?paysLabel ?date
```