# D08 Apple Stock — Séries temporelles

- **Énoncé d'origine** : `exercices/drills/originaux/08_Time_Series/Apple_Stock/`
- **Données locales** : donnees/drills/appl_1980_2014.csv (aussi dans le dossier de l'exercice)
- **Place dans le cours** : Approfondissement A1

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `apple`.
4. Vérifier le type des colonnes.
5. Convertir la colonne `Date` en date.
6. Utiliser la date comme index.
7. Y a-t-il des dates en double ?
8. L'index commence par la date la plus récente. Faire en sorte que la première ligne soit la plus ancienne.
9. Obtenir le dernier jour ouvré de chaque mois.
10. Quelle est la différence en jours entre la première et la dernière date ?
11. Combien de mois couvrent les données ?
12. Tracer la valeur `Adj Close`, avec une figure de 13,5 × 9 pouces.
13. Bonus : formuler votre propre question et y répondre.

## Remarques

- Étapes 9 et 11 : l'alias `BM` a été supprimé ; l'alias actuel est `BME`.
