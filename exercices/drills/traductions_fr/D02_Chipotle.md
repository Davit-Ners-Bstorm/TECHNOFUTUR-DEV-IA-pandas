# D02 Chipotle — Filtrer et trier

- **Énoncé d'origine** : `exercices/drills/originaux/02_Filtering_&_Sorting/Chipotle/`
- **Données locales** : donnees/drills/chipotle.tsv
- **Place dans le cours** : Chapitre 4

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `chipo`.
4. Combien de produits coûtent plus de 10 $ ?
5. Quel est le prix de chaque article ? Afficher un DataFrame avec seulement les deux colonnes `item_name` et `item_price`.
6. Trier par nom d'article.
7. Quelle était la quantité de l'article le plus cher commandé ?
8. Combien de fois un « Veggie Salad Bowl » a-t-il été commandé ?
9. Combien de fois quelqu'un a-t-il commandé plus d'une « Canned Soda » ?

## Remarques

- L'étape 4 est ambiguë : le prix `item_price` est le prix de la ligne, quantité comprise. Précisez ce que vous comptez (produits distincts, lignes de commande) avant de répondre.
