# Population des pays

La présente requête concerne tous les pays du monde et affiche leur nom, leur nombre d'habitants sur trente ans (1993 - 2023) et leur code CIO. Pour plus de détails, veuillez consulter le [journal de bord](../Journal-de-bord/Journal-de-bord.pdf).

Pour tester la requête : [Wikidata : Service des requêtes SPARQL](https://w.wiki/8uTN).

```sparql
SELECT ?paysLabel ?population ?date ?cio
WHERE 
{
  ?pays wdt:P31 wd:Q6256.
  ?pays wdt:P984 ?cio.
  ?pays p:P1082 ?populationStatement.
  ?populationStatement ps:P1082 ?population.
  ?populationStatement pq:P585 ?date.
  FILTER(YEAR(?date) >= (YEAR(NOW()) - 30)).
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }
           }
ORDER BY ?paysLabel ?date
```
