# Exercice JO — informations pratiques

- **Énoncé** : `Pandas_JO_FR_v2.pdf` (32 questions).
- **Données** : `donnees/bstorm/Exercices_Pandas_athlete_events.csv` à la racine du projet. Depuis un notebook placé dans ce dossier : `pd.read_csv("../../../donnees/bstorm/Exercices_Pandas_athlete_events.csv")`.
- **Une ligne du fichier** = une participation d'un athlète à une épreuve, lors d'une édition des Jeux.

## Répartition dans le cours

| Questions | Chapitre |
|---|---|
| 1 à 8 | 3 — Importer, exporter, découvrir |
| 9 à 16 | 4 — Sélectionner, filtrer, trier |
| 17 à 22 | 5 — Nettoyer |
| 23 à 32 | 7 — GroupBy et tableaux croisés |

## Précisions sur l'énoncé

- Question 9 : la colonne « Edition » s'appelle `Games` dans le fichier.
- « Pays » peut désigner `Team` (nom de l'équipe) ou `NOC` (code du comité national). `NOC` est plus fiable : une même nation peut avoir plusieurs noms d'équipe.
- Questions 23 à 32 : décidez si vous comptez des **médaillés** (lignes) ou des **médailles** (une par épreuve, par édition et par équipe). Le chapitre 7 montre la différence.
