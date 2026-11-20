# Exercice API météo — informations pratiques

Deux énoncés existent dans ce dossier :

- `call_api_meteo.ipynb` : prévisions sur 7 jours pour **toutes les communes de Bruxelles**, avec les codes postaux de l'Open Data Wallonie-Bruxelles (ODWB) ;
- `enoncé.txt` : **sept communes** listées, trois variables (température, probabilité de précipitation, vent à 10 m), un CSV final et au moins une fonction `f(url_commune) -> DataFrame`.

Le cours prend `enoncé.txt` comme référence ; le notebook constitue une extension.

- **Codes postaux et coordonnées** : `donnees/api/communes_belges_lon_lat.csv` (fichier produit par la correction Bstorm), utilisable sans appeler l'API ODWB.
- **API météo** : Open-Meteo, gratuite et sans clé (`https://api.open-meteo.com/v1/forecast`).
- **Sans connexion Internet** : `donnees/api/exemple_reponse_open_meteo_valeurs_fictives.json` contient une réponse d'exemple (structure réelle de l'API, valeurs fictives) pour 7 communes.
- Notions utiles : chapitre 9 (`json_normalize`, `explode` sur plusieurs colonnes à la fois), chapitre 11 (`requests`).
