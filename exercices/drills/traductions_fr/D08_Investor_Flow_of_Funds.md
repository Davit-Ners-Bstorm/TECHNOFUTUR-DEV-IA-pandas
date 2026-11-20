# D08 Investor Flow of Funds — Séries temporelles

- **Énoncé d'origine** : `exercices/drills/originaux/08_Time_Series/Investor_Flow_of_Funds_US/`
- **Données locales** : aucune : le fichier source en ligne ne contient plus que sa ligne d'en-tête
- **Place dans le cours** : Annexe (données indisponibles)

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable.
4. Quelle est la fréquence du jeu de données ?
5. Utiliser la colonne `Date` comme index.
6. Quel est le type de l'index ?
7. Convertir l'index en `DatetimeIndex`.
8. Passer à une fréquence mensuelle en faisant la somme, et l'affecter à `monthly`.
9. Les mois sans données apparaissent avec des `NaN` : supprimer ces lignes.
10. Passer maintenant à une fréquence annuelle.
11. Bonus : formuler votre propre question et y répondre.

## Remarques

- Le fichier en ligne a été vidé par son auteur (seul l'en-tête subsiste) : l'exercice ne peut plus être réalisé.
- L'étape 9 repose sur une hypothèse devenue fausse : la somme d'un mois vide vaut 0, pas `NaN`. Les notions (alias `ME`, `YS`) sont couvertes par l'approfondissement A1.
