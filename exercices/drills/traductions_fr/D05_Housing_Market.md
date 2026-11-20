# D05 Housing Market — Assembler des tables

- **Énoncé d'origine** : `exercices/drills/originaux/05_Merge/Housing Market/`
- **Données locales** : données aléatoires créées dans le notebook
- **Place dans le cours** : Chapitre 8

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Créer 3 Series de longueur 100 : la première avec des nombres aléatoires de 1 à 4, la deuxième de 1 à 3, la troisième de 10 000 à 30 000.
3. Créer un DataFrame en réunissant les Series en colonnes.
4. Renommer les colonnes en `bedrs`, `bathrs`, `price_sqr_meter`.
5. Créer un DataFrame d'une seule colonne contenant les valeurs des 3 Series, et l'affecter à `bigcolumn`.
6. L'index semble s'arrêter à 99. Est-ce vrai ?
7. Réindexer le DataFrame pour qu'il aille de 0 à 299.
