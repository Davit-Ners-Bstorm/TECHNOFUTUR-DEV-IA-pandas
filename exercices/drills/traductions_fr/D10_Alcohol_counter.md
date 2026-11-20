# D10 Alcohol counter — Indexation

- **Énoncé d'origine** : `exercices/drills/originaux/10_Indexing/Alcohol_counter/`
- **Données locales** : donnees/drills/drinksbycountry.csv (le lien raccourci bit.ly de l'énoncé pointe vers ce fichier)
- **Place dans le cours** : Chapitre 4 (approfondissement de l'index)

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `drinks`.
4. Afficher les 5 premières lignes.
5. Afficher l'index.
6. Identifier les lignes concernées (par exemple les pays d'Europe).
7. Utiliser `.loc` pour récupérer une cellule.
8. Utiliser `.iloc` pour récupérer une ou plusieurs lignes.
9. Utiliser `country` comme index.
10. Sélectionner une cellule avec ce nouvel index.
11. Effacer le nom de l'index.
12. Redonner un nom à l'index et le remettre en colonne.
13. Utiliser l'index pour sélectionner des valeurs dans une Series.
14. Trier selon les valeurs de la Series.
15. Bonus : réindexer pour aligner sur d'autres objets.

## Remarques

- Plusieurs étapes sont formulées de façon vague (« identifier les lignes », « un index plus complexe ») : le fichier `Guidelines_Results.ipynb` montre le résultat attendu.
