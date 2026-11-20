# D08 Getting Financial Data — Séries temporelles

- **Énoncé d'origine** : `exercices/drills/originaux/08_Time_Series/Getting_Financial_Data/`
- **Données locales** : aucune
- **Place dans le cours** : Annexe (non exécutable)

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Créer une période : du 01/01/2015 à aujourd'hui.
3. Sélectionner les symboles boursiers d'Apple, Tesla, Twitter, IBM et LinkedIn, dans une variable `stocks`.
4. Lire les données depuis le service en ligne, les affecter à `df` et les afficher.
5. Quel est le type de structure de `df` ?
6. Afficher toutes les valeurs de l'axe `Items`.
7. Créer un DataFrame `vol` avec les volumes échangés.
8. Agréger les volumes par semaine, sans mélanger les semaines de différentes années.
9. Calculer le volume total échangé en 2015.
10. Bonus : formuler votre propre question et y répondre.

## Remarques

- Cet exercice ne peut plus être exécuté : la structure `Panel` a été supprimée de Pandas (version 1.0), le service de données utilisé par `pandas_datareader` n'est plus disponible, et plusieurs symboles (LinkedIn, Twitter) ne sont plus cotés. Il est conservé en annexe pour mémoire.
