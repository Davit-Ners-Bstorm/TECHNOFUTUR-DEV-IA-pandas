# D02 Fictional Army — Filtrer et trier

- **Énoncé d'origine** : `exercices/drills/originaux/02_Filtering_&_Sorting/Fictional Army/`
- **Données locales** : données créées dans le notebook (dictionnaire)
- **Place dans le cours** : Chapitre 4

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Les données sont fournies sous forme de dictionnaire (voir le notebook).
3. Créer un DataFrame nommé `army`, en conservant l'ordre des colonnes du dictionnaire (`regiment`, `company`, `deaths`…).
4. Utiliser la colonne `origin` comme index.
5. Afficher uniquement la colonne `veterans`.
6. Afficher les colonnes `veterans` et `deaths`.
7. Afficher le nom de toutes les colonnes.
8. Sélectionner les colonnes `deaths`, `size` et `deserters` pour le Maine et l'Alaska.
9. Sélectionner les lignes 3 à 7 et les colonnes 3 à 6.
10. Sélectionner toutes les lignes après la quatrième, et toutes les colonnes.
11. Sélectionner toutes les lignes jusqu'à la quatrième, et toutes les colonnes.
12. Sélectionner de la 3e à la 7e colonne.
13. Sélectionner les lignes où `deaths` est supérieur à 50.
14. Sélectionner les lignes où `deaths` est supérieur à 500 ou inférieur à 50.
15. Sélectionner tous les régiments qui ne s'appellent pas « Dragoons ».
16. Sélectionner les lignes nommées Texas et Arizona.
17. Sélectionner la troisième cellule de la ligne nommée Arizona.
18. Sélectionner la troisième cellule de la colonne `deaths`.

## Remarques

- L'énoncé indique que Pandas trierait les colonnes par ordre alphabétique : ce n'est plus le cas depuis Python 3.7, l'ordre du dictionnaire est conservé.
- « lignes 3 à 7 » : décidez si l'énoncé compte à partir de 1 ou de 0, et si la borne est incluse (chapitre 4, `iloc`).
