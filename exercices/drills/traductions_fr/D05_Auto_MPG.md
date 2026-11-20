# D05 Auto MPG — Assembler des tables

- **Énoncé d'origine** : `exercices/drills/originaux/05_Merge/Auto_MPG/`
- **Données locales** : donnees/drills/cars1.csv et cars2.csv (aussi dans le dossier de l'exercice)
- **Place dans le cours** : Chapitre 8

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer les deux jeux de données `cars1` et `cars2`.
3. Les affecter à deux variables `cars1` et `cars2`.
4. Le premier jeu de données contient des colonnes vides sans nom : corriger `cars1`.
5. Quel est le nombre d'observations de chaque jeu de données ?
6. Réunir `cars1` et `cars2` en un seul DataFrame nommé `cars`.
7. Il manque une colonne `owners`. Créer une Series de nombres aléatoires entre 15 000 et 73 000.
8. Ajouter la colonne `owners` à `cars`.

## Remarques

- Étape 6 : `DataFrame.append` a été supprimé en Pandas 2 ; utilisez `pd.concat` (chapitre 8).
- Étape 8 : après `concat`, l'index contient des doublons ; une Series alignée sur l'index ne donnerait pas le résultat attendu. Pensez à `ignore_index`.
