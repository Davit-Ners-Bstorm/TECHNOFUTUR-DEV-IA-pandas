# D03 Regiment — Regrouper

- **Énoncé d'origine** : `exercices/drills/originaux/03_Grouping/Regiment/`
- **Données locales** : données créées dans le notebook
- **Place dans le cours** : Chapitre 7

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Créer le DataFrame avec les valeurs fournies.
3. L'affecter à une variable nommée `regiment`, en nommant chaque colonne.
4. Quelle est la moyenne de `preTestScore` du régiment Nighthawks ?
5. Afficher les statistiques générales par compagnie (`company`).
6. Quelle est la moyenne de `preTestScore` de chaque compagnie ?
7. Afficher la moyenne de `preTestScore` par régiment et par compagnie.
8. Même question, sans index hiérarchique.
9. Regrouper tout le DataFrame par régiment et par compagnie.
10. Quel est le nombre d'observations par régiment et par compagnie ?
11. Parcourir les groupes et afficher le nom et les données de chaque régiment.

## Remarques

- Étapes 4 et 9 : les colonnes `name` et `company` sont du texte. En Pandas 3, une moyenne sur tout le DataFrame groupé lève une erreur ; sélectionnez les colonnes numériques.
