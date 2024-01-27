# Requête SPARQL (régions du Royaume-Uni)

La présente requête concerne les régions du Royaume-Uni et affiche leur nom, leur nombre d'habitants et leurs coordonnées. Pour plus de détails, veuillez consulter le [journal de bord](../Journal-de-bord/Journal-de-bord.pdf).

Pour tester la requête : [Wikidata : Service des requêtes SPARQL](https://w.wiki/8ynk).

```sparql
SELECT ?RegionLabel ?population ?geopoint
WHERE 
{
  ?Region wdt:P31 wd:Q36784.
  ?Region wdt:P1082 ?population.
  ?Region wdt:P625 ?geopoint.
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }
           }
ORDER BY ?Region
```
