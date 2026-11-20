# D05 Fictitious Names — Assembler des tables

- **Énoncé d'origine** : `exercices/drills/originaux/05_Merge/Fictitous Names/`
- **Données locales** : données créées dans le notebook
- **Place dans le cours** : Chapitre 8

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Créer les 3 DataFrame à partir des données fournies.
3. Les affecter à trois variables `data1`, `data2`, `data3`.
4. Réunir les deux premiers DataFrame selon les lignes, dans `all_data`.
5. Réunir les deux premiers DataFrame selon les colonnes, dans `all_data_col`.
6. Afficher `data3`.
7. Joindre `all_data` et `data3` sur la colonne `subject_id`.
8. Joindre uniquement les données dont le `subject_id` est présent dans `data1` et `data2`.
9. Joindre toutes les valeurs de `data1` et `data2`, en associant les enregistrements des deux côtés quand c'est possible.

## Remarques

- La page citée dans l'introduction (explication visuelle des jointures SQL) correspond au schéma du chapitre 8.
