# D06 US Baby Names — Statistiques

- **Énoncé d'origine** : `exercices/drills/originaux/06_Stats/US_Baby_Names/`
- **Données locales** : donnees/drills/US_Baby_Names_right.csv (36 Mo)
- **Place dans le cours** : Chapitre 6

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `baby_names`.
4. Afficher les 10 premières lignes.
5. Supprimer les colonnes `Unnamed: 0` et `Id`.
6. Y a-t-il plus de prénoms masculins ou féminins dans le jeu de données ?
7. Regrouper le jeu de données par prénom et l'affecter à `names`.
8. Combien de prénoms différents existe-t-il ?
9. Quel est le prénom le plus fréquent ?
10. Combien de prénoms différents ont le nombre d'occurrences minimal ?
11. Quel est le nombre médian d'occurrences d'un prénom ?
12. Quel est l'écart-type du nombre d'occurrences ?
13. Obtenir un résumé avec la moyenne, le minimum, le maximum, l'écart-type et les quartiles.

## Remarques

- Étape 7 : en Pandas 3, sommer par prénom toutes les colonnes concatène les colonnes texte (`Gender`, `State`). Sélectionnez la colonne `Count`.
