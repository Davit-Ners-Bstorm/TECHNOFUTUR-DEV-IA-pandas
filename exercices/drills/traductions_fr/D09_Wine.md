# D09 Wine — Supprimer des données

- **Énoncé d'origine** : `exercices/drills/originaux/09_Deleting/Wine/`
- **Données locales** : donnees/drills/wine.data (copie locale au format UCI, sans en-tête)
- **Place dans le cours** : Approfondissement (chapitre 5)

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `wine`.
4. Supprimer les colonnes 1, 4, 7, 9, 11, 13 et 14.
5. Nommer les colonnes restantes : `alcohol`, `malic_acid`, `alcalinity_of_ash`, `magnesium`, `flavanoids`, `proanthocyanins`, `hue`.
6. Mettre à `NaN` les 3 premières valeurs de `alcohol`.
7. Mettre à `NaN` les lignes 3 et 4 de `magnesium`.
8. Remplacer les `NaN` par 10 dans `alcohol` et par 100 dans `magnesium`.
9. Compter le nombre de valeurs manquantes.
10. Créer un tableau de 10 nombres aléatoires inférieurs à 10.
11. Utiliser ces nombres comme positions de lignes et mettre `NaN` dans les cellules correspondantes de `alcohol`.
12. Combien de valeurs manquantes y a-t-il maintenant ?
13. Supprimer les lignes qui contiennent des valeurs manquantes.
14. Afficher uniquement les valeurs non nulles de `alcohol`.
15. Réinitialiser l'index pour qu'il recommence à 0.
16. Bonus : formuler votre propre question et y répondre.

## Remarques

- Lire le fichier avec `header=None` (pas de ligne d'en-tête).
- Étapes 8 et 11 : les écritures `wine.alcohol.fillna(..., inplace=True)` et `wine.alcohol[random] = np.nan` ne modifient plus rien en Pandas 3. Utilisez `wine['alcohol'] = ...` et `wine.loc[...]` (chapitre 5).
- Étape 7 : « lignes 3 et 4 » : précisez si vous comptez à partir de 0 ou de 1.
