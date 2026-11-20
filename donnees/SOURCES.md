# Provenance des données

## `bstorm/` — données des exercices Bstorm

| Fichier | Origine | Remarque |
|---|---|---|
| `Exercices_Pandas_athlete_events.csv` | archives Bstorm (exercice JO) ; jeu « 120 years of Olympic history » (Kaggle, R. Griffin) | 271 116 lignes, 15 colonnes ; une ligne = une participation d'un athlète à une épreuve |
| `sakila.xlsx` | archives Bstorm (exercice Sakila) ; extrait de la base exemple Sakila (MySQL) | 5 feuilles ; contient une colonne `Unnamed: 0` issue d'un export avec l'index |

## `demo/` — jeu de démonstration du cours

Données **fictives**, générées pour le cours (graine fixe, reproductibles). Elles contiennent volontairement des défauts à traiter.

| Fichier | Contenu | Défauts volontaires |
|---|---|---|
| `clients.csv` | 30 clients (identifiants 101 à 130), ville, segment, âge, date d'inscription | 3 âges manquants ; clients 127 à 130 sans commande |
| `produits.csv` | 15 produits (P01 à P15), catégorie, prix | |
| `commandes.csv` | 240 commandes de l'année 2025 | identifiants client 999 et 998 inexistants (22 commandes) |
| `commandes_brutes.csv` | les mêmes commandes, telles qu'exportées par un autre système | séparateur `;`, prix `"79,00 €"`, canaux écrits de plusieurs façons, quantité `"deux"`, valeurs manquantes, 3 lignes en double |
| `capteurs_salle_b12.csv` | température et humidité horaires d'une salle, du 1er au 21 mars 2025 | 12 mesures de température manquantes |

## `drills/` — données des exercices d'entraînement

Copies locales des fichiers que les énoncés téléchargent, pour travailler sans connexion.

| Fichier | Origine |
|---|---|
| `chipotle.tsv`, `drinks.csv`, `u.user` | dépôt GitHub `justmarkham/DAT8` |
| `drinksbycountry.csv` | même contenu que `drinks.csv` avec les continents en toutes lettres ; cible du lien `bit.ly/drinksbycountry` de l'énoncé D10 |
| `Euro_2012_stats_TEAM.csv`, `student-mat.csv`, `US_Crime_Rates_1960_2014.csv`, `cars1.csv`, `cars2.csv`, `US_Baby_Names_right.csv`, `wind.data`, `appl_1980_2014.csv` | dépôt GitHub `guipsamora/pandas_exercises` |
| `iris.data`, `wine.data` | reconstitués au format UCI (sans en-tête, mêmes valeurs) à partir des copies distribuées avec seaborn et scikit-learn, le serveur UCI n'étant pas joignable lors de la préparation |

Drills sans données locales (voir `annexes/README.md`) : World Food Facts (fichier Kaggle à télécharger manuellement), Getting Financial Data (service disparu), Investor Flow of Funds (fichier source désormais vide).

## `api/` — exercice API météo

| Fichier | Origine |
|---|---|
| `communes_belges_lon_lat.csv` | archives Bstorm (`data_cleaned`) : codes postaux, communes, coordonnées |
| `communes_exemple.csv` | extrait de 7 communes du fichier précédent |
| `exemple_reponse_open_meteo_valeurs_fictives.json` | réponse au format de l'API Open-Meteo, **valeurs fictives**, utilisée quand l'API n'est pas joignable |

## `chunk/` — exercice chunk processing

| Fichier | Origine |
|---|---|
| `nov_synthetique.zip` | **données synthétiques** : 400 000 lignes générées avec le schéma exact du fichier Kaggle « eCommerce behavior data from multi category store » (`nov.zip`, 2,87 Go) ; colonnes `event_time`, `event_type`, `product_id`, `category_id`, `category_code`, `brand`, `price`, `user_id`, `user_session` |

Le fichier d'origine peut remplacer le fichier synthétique sans autre modification que le chemin.
