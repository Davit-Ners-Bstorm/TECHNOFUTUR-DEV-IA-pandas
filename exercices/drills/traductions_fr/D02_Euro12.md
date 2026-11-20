# D02 Euro12 — Filtrer et trier

- **Énoncé d'origine** : `exercices/drills/originaux/02_Filtering_&_Sorting/Euro12/`
- **Données locales** : donnees/drills/Euro_2012_stats_TEAM.csv (aussi dans le dossier de l'exercice)
- **Place dans le cours** : Chapitre 4

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `euro12`.
4. Sélectionner uniquement la colonne `Goals`.
5. Combien d'équipes ont participé à l'Euro 2012 ?
6. Quel est le nombre de colonnes ?
7. Afficher uniquement les colonnes `Team`, `Yellow Cards` et `Red Cards`, et les affecter à un DataFrame nommé `discipline`.
8. Trier les équipes par cartons rouges, puis par cartons jaunes.
9. Calculer la moyenne des cartons jaunes par équipe.
10. Filtrer les équipes qui ont marqué plus de 6 buts.
11. Sélectionner les équipes dont le nom commence par G.
12. Sélectionner les 7 premières colonnes.
13. Sélectionner toutes les colonnes sauf les 3 dernières.
14. Afficher uniquement la précision de tir (`Shooting Accuracy`) de l'Angleterre, de l'Italie et de la Russie.

## Remarques

- Les noms de colonnes contiennent des espaces : la notation pointée (`euro12.Yellow Cards`) est impossible, utilisez les crochets.
