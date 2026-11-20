# D01 Chipotle — Découvrir un jeu de données

- **Énoncé d'origine** : `exercices/drills/originaux/01_Getting_&_Knowing_Your_Data/Chipotle/`
- **Données locales** : donnees/drills/chipotle.tsv (séparateur tabulation)
- **Place dans le cours** : Chapitres 3 et 5

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée dans le notebook (copie locale : voir ci-dessus).
3. L'affecter à une variable nommée `chipo`.
4. Afficher les 10 premières lignes.
5. Quel est le nombre d'observations du jeu de données ?
6. Quel est le nombre de colonnes ?
7. Afficher le nom de toutes les colonnes.
8. Comment le jeu de données est-il indexé ?
9. Quel est l'article (`item_name`) le plus commandé ?
10. Pour cet article, combien d'unités ont été commandées ?
11. Quel est l'article le plus commandé dans la colonne `choice_description` ?
12. Combien d'articles ont été commandés au total ?
13. Convertir le prix de l'article en nombre décimal : a) vérifier le type de `item_price` ; b) créer une fonction lambda et changer le type de `item_price` ; c) vérifier à nouveau le type.
14. Quel est le chiffre d'affaires sur la période couverte par le jeu de données ?
15. Combien de commandes ont été passées sur la période ?
16. Quel est le montant moyen par commande ?
17. Combien d'articles différents sont vendus ?

## Remarques

- En Pandas 3, le texte est de type `str` : un `groupby(...).sum()` sur toutes les colonnes concatène les textes, et une moyenne sur ces colonnes lève une erreur. Sélectionnez les colonnes numériques avant d'agréger (chapitre 7).
- Le prix est écrit sous la forme `$2.39 ` : pensez au symbole et à l'espace final.
