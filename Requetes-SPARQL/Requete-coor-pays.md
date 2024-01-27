# Requête SPARQL (coordonnées)

La présente requête concerne tous les pays du monde et affiche leur nom, leurs coordonnées et leur code CIO. Pour plus de détails, veuillez consulter le [journal de bord](../Journal-de-bord/Journal-de-bord.pdf).

Pour tester la requête : [Wikidata : Service des requêtes SPARQL](https://w.wiki/8yne).

```sparql
SELECT DISTINCT ?paysLabel ?geopoint ?noc
WHERE 
{
  ?pays wdt:P31 wd:Q6256.
  ?pays wdt:P984 ?noc.
  ?pays wdt:P625 ?geopoint.
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
