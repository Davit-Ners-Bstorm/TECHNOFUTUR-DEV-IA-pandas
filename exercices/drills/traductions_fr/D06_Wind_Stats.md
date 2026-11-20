# D06 Wind Stats — Statistiques sur une série temporelle

- **Énoncé d'origine** : `exercices/drills/originaux/06_Stats/Wind_Stats/`
- **Données locales** : donnees/drills/wind.data (aussi dans le dossier de l'exercice), séparateur : espaces
- **Place dans le cours** : Approfondissement A1

Le chemin d'un fichier local se donne relativement au notebook. Depuis le dossier de l'exercice, la racine du projet est cinq niveaux plus haut, par exemple `../../../../../donnees/drills/`.

## Étapes

1. Importer les bibliothèques nécessaires.
2. Importer le jeu de données depuis l'adresse indiquée.
3. L'affecter à une variable nommée `data` et remplacer les 3 premières colonnes par un véritable index de dates.
4. Année 2061 ? Avons-nous vraiment des données de cette année ? Écrire une fonction pour corriger et l'appliquer.
5. Utiliser les dates corrigées comme index. Attention au type : il doit être `datetime64`.
6. Calculer le nombre de valeurs manquantes par station sur toute la période (elles seront ignorées dans tous les calculs suivants).
7. Calculer le nombre total de valeurs non manquantes.
8. Calculer la vitesse moyenne du vent sur toutes les stations et toute la période : un seul nombre.
9. Créer un DataFrame `loc_stats` avec le minimum, le maximum, la moyenne et l'écart-type par station sur tous les jours.
10. Créer un DataFrame `day_stats` avec le minimum, le maximum, la moyenne et l'écart-type de toutes les stations, pour chaque jour.
11. Calculer la vitesse moyenne en janvier pour chaque station (janvier 1961 et janvier 1962 comptent tous deux comme « janvier »).
12. Ré-échantillonner à une fréquence annuelle pour chaque station.
13. Ré-échantillonner à une fréquence mensuelle pour chaque station.
14. Ré-échantillonner à une fréquence hebdomadaire pour chaque station.
15. Calculer le minimum, le maximum, la moyenne et l'écart-type de toutes les stations pour chaque semaine (la première semaine commence le 2 janvier 1961), pour les 52 premières semaines.

## Remarques

- Le texte d'introduction précise que tout doit se faire sans boucle `for`.
- Étape 3 : `parse_dates=[[0, 1, 2]]` a été supprimé en Pandas 3. Voir l'approfondissement A1, section 8.
- Étapes 12 à 14 : utilisez les alias actuels (`YE`, `ME`, `W`).
