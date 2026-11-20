# D04 US Crime Rates — Séries temporelles

- **Énoncé d'origine** : `exercices/drills/originaux/04_Apply/US_Crime_Rates/`
- **Données locales** : donnees/drills/US_Crime_Rates_1960_2014.csv (aussi dans le dossier de l'exercice)
- **Place dans le cours** : Approfondissement A1

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `crime`.
4. Quel est le type des colonnes ?
5. La colonne `Year` est de type `int64`, alors que Pandas dispose d'un type dédié aux dates. Convertir `Year` en `datetime64`.
6. Utiliser `Year` comme index.
7. Supprimer la colonne `Total`.
8. Regrouper les années par décennie et faire la somme des valeurs. Attention à la colonne `Population` : la sommer serait une erreur.
9. Quelle a été la décennie la plus dangereuse aux États-Unis ?

## Remarques

- Étape 5 : convertir des entiers avec `format=` affiche un avertissement en Pandas 3.1 ; convertissez d'abord en texte (`astype(str)`).
- Étape 8 : l'alias `10AS` a été supprimé ; l'alias actuel est `10YS` (approfondissement A1).
