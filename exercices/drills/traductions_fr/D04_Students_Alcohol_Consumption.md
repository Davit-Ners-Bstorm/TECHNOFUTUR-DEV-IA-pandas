# D04 Students Alcohol Consumption — Appliquer des fonctions

- **Énoncé d'origine** : `exercices/drills/originaux/04_Apply/Students_Alcohol_Consumption/`
- **Données locales** : donnees/drills/student-mat.csv (aussi dans le dossier de l'exercice)
- **Place dans le cours** : Chapitre 10

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `df`.
4. Pour cet exercice, découper le DataFrame de la colonne `school` jusqu'à la colonne `guardian`.
5. Créer une fonction lambda qui met une majuscule initiale à une chaîne.
6. Appliquer cette majuscule aux colonnes `Mjob` et `Fjob`.
7. Afficher les dernières lignes du jeu de données.
8. Avez-vous remarqué que le DataFrame est toujours en minuscules ? Pourquoi ? Corriger, et mettre la majuscule à `Mjob` et `Fjob`.
9. Créer une fonction `majority` qui renvoie un booléen, stocké dans une nouvelle colonne `legal_drinker` (on considère la majorité à partir de 18 ans, soit plus de 17 ans).
10. Multiplier chaque nombre du jeu de données par 10 (l'opération n'a pas de sens, c'est un exercice).

## Remarques

- Étape 10 : `applymap` n'existe plus en Pandas 3 ; la méthode s'appelle `DataFrame.map`.
- Étape 8 : la sélection de l'étape 4 est une copie. Pensez au chapitre 5 (Copy-on-Write) pour modifier le bon objet.
