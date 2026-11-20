# D09 Iris — Supprimer des données

- **Énoncé d'origine** : `exercices/drills/originaux/09_Deleting/Iris/`
- **Données locales** : donnees/drills/iris.data (copie locale au format UCI, sans en-tête)
- **Place dans le cours** : Chapitre 5

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `iris`.
4. Donner un nom aux colonnes.
5. Y a-t-il des valeurs manquantes dans le DataFrame ?
6. Mettre à `NaN` les valeurs des lignes 10 à 29 de la colonne `petal_length`.
7. Remplacer ces `NaN` par 1.0.
8. Supprimer la colonne `class`.
9. Mettre les 3 premières lignes à `NaN`.
10. Supprimer les lignes qui contiennent des `NaN`.
11. Réinitialiser l'index pour qu'il recommence à 0.
12. Bonus : formuler votre propre question et y répondre.

## Remarques

- Le fichier `iris.data` n'a pas de ligne d'en-tête : lisez-le avec `header=None`, sinon la première fleur devient le nom des colonnes.
- Étape 7 : `iris.petal_length.fillna(1, inplace=True)` ne modifie plus rien en Pandas 3 (chapitre 5, Copy-on-Write).
