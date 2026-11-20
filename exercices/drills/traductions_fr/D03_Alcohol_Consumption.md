# D03 Alcohol Consumption — Regrouper

- **Énoncé d'origine** : `exercices/drills/originaux/03_Grouping/Alcohol_Consumption/`
- **Données locales** : donnees/drills/drinks.csv
- **Place dans le cours** : Chapitre 7

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `drinks`.
4. Quel continent boit le plus de bière en moyenne ?
5. Pour chaque continent, afficher les statistiques de consommation de vin.
6. Afficher la consommation moyenne d'alcool par continent, pour chaque colonne.
7. Afficher la consommation médiane d'alcool par continent, pour chaque colonne.
8. Afficher la moyenne, le minimum et le maximum de consommation de spiritueux, sous forme de DataFrame.

## Remarques

- Étapes 6 et 7 : la colonne `country` est du texte. En Pandas 3, `groupby(...).mean()` sur toutes les colonnes lève une erreur ; utilisez `numeric_only=True` ou sélectionnez les colonnes numériques.
- Dans `drinks.csv`, le code de continent `NA` (Amérique du Nord) est lu comme une valeur manquante par défaut : vérifiez `drinks['continent'].isna().sum()`.
