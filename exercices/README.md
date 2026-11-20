# Exercices

## Organisation

| Dossier | Contenu |
|---|---|
| `bstorm/` | exercices Bstorm d'origine (énoncés inchangés) et une note `LISEZMOI.md` par exercice |
| `drills/originaux/` | exercices d'entraînement d'origine, en anglais : énoncé (`Exercises.ipynb`) et résultats attendus (`Guidelines_Output.ipynb`) |
| `drills/traductions_fr/` | traduction française de chaque drill, avec les données locales et les points d'attention |
| `supplementaires/` | exercices courts propres à ce cours (S01 à S12) |

Les corrections sont dans le dossier `corrections/` à la racine du projet.

Les données sont centralisées dans `donnees/` à la racine. Depuis un notebook, un chemin se donne relativement à l'emplacement du notebook.

## Exercices par chapitre

| Chapitre | Exercices Bstorm | Supplémentaires | Drills |
|---|---|---|---|
| 1 — Series | | S01 | |
| 2 — DataFrame | | | D07 Pokemon |
| 3 — Importer, exporter, découvrir | JO, questions 1 à 8 | | D01 Occupation, D01 Chipotle (étapes 1 à 12) |
| 4 — Sélectionner, filtrer, trier | JO, questions 9 à 16 | S04 | D02 Euro12, D02 Fictional Army, D02 Chipotle, D10 Alcohol counter |
| 5 — Nettoyer | JO, questions 17 à 22 ; Sakila, questions 1 à 7 | S05 | D01 Chipotle (étapes 13 à 17), D09 Iris, D09 Wine |
| 6 — Statistiques et agrégations | JO, questions 18, 19, 29 | | D06 US Baby Names |
| 7 — GroupBy et tableaux croisés | JO, questions 23 à 32 ; Sakila, questions 9 et 10 | S07 | D03 Alcohol Consumption, D03 Occupation, D03 Regiment |
| 8 — Jointures et concaténation | Sakila, questions 8 et 11 à 14 | S08 | D05 Fictitious Names, D05 Auto MPG, D05 Housing Market |
| 9 — Restructurer | | S09 | |
| 10 — `map`, `apply`, vectorisation | | S10 | D04 Students Alcohol Consumption |
| 11 — Pandas connecté | SQLAlchemy iris ; API météo | | |
| 12 — Synthèse | | S12 | |
| A1 — Séries temporelles | | | D04 US Crime Rates, D06 Wind Stats, D08 Apple Stock |
| A2 — Gros volumes | chunk processing | | |
| A3 — SQL avancé | Sakila en version SQL | | |

Les drills D01 World Food Facts, D08 Getting Financial Data et D08 Investor Flow of Funds ne peuvent plus être réalisés tels quels (données à télécharger manuellement, service ou données disparus). Ils sont conservés, voir `annexes/`.

## Format des exercices supplémentaires

Les exercices supplémentaires sont numérotés d'après leur chapitre (S01 pour le chapitre 1, S04 pour le chapitre 4…). Chaque exercice suit la même structure : **Énoncé**, **Règles et étapes**, **Objectifs pédagogiques**, **Mockup** (forme du résultat attendu), **Contraintes**. La correction est fournie séparément.
