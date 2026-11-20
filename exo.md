# Exercice — Gestion des employés d'une entreprise

**Objectif :** construire et manipuler un DataFrame Pandas représentant les employés d'une entreprise.

## Contexte

Une entreprise souhaite analyser les informations de ses employés : salaires, ancienneté et départements.

Vous devez construire un tableau de données, effectuer différents calculs et examiner sa structure à l'aide de Pandas.

## 1. Création du DataFrame

À partir des données suivantes, créez un DataFrame nommé `df_employes`.

| Nom | Département | Salaire mensuel (€) | Ancienneté (années) |
|---|---|---:|---:|
| Alice | IT | 3 200 | 4 |
| Bob | RH | 2 800 | 2 |
| Charlie | IT | 3 800 | 6 |
| Diana | Marketing | 3 000 | 3 |
| Ethan | IT | 4 200 | 8 |
| Fatima | RH | 3 100 | 5 |

**Consignes :**
- Utilisez un dictionnaire Python pour construire le DataFrame.
- Affichez le DataFrame.
- Vérifiez que les colonnes portent les bons noms.

## 2. Explorer la structure

Sans modifier les données :

1. Affichez le nombre de lignes et de colonnes.
2. Affichez les noms des colonnes.
3. Affichez les types de données de chaque colonne.
4. Affichez les index du DataFrame.
5. Récupérez uniquement la colonne `Salaire mensuel (€)` dans une variable `salaires`.

**Question :** quel est le type de `salaires` ? Est-ce encore un DataFrame ?

## 3. Ajouter des colonnes calculées

Complétez le DataFrame avec les colonnes suivantes :

1. `Salaire annuel (€)` : salaire mensuel multiplié par 12.
2. `Prime (€)` : prime annuelle de 500 € par année d'ancienneté.
3. `Rémunération totale (€)` : salaire annuel augmenté de la prime.
4. `Coût employeur (€)` : rémunération totale augmentée de 25 %.

Effectuez les calculs directement sur les colonnes Pandas, sans utiliser de boucle `for`.

Affichez le DataFrame avec ses nouvelles colonnes.

## 4. Statistiques et opérations

À l'aide des colonnes du DataFrame :

1. Calculez le salaire mensuel moyen.
2. Trouvez le salaire mensuel le plus élevé et le plus faible.
3. Calculez le coût employeur total annuel de l'entreprise.
4. Calculez la différence de salaire mensuel entre chaque employé et le salaire moyen.
5. Ajoutez cette différence au DataFrame dans une colonne `Écart moyenne (€)`.

## 5. Manipuler les index

Créez un **nouveau DataFrame**, à partir de `df_employes`, dont les index sont les noms des employés, sans modifier le DataFrame original.

1. Affichez ses index.
2. Récupérez la colonne des salaires mensuels.
3. Créez une `Series` contenant les valeurs suivantes, avec les index correspondants :

| Index | Montant |
|---|---:|
| Alice | 100 |
| Charlie | 200 |
| Ethan | 300 |

4. Additionnez cette Series à la colonne des salaires mensuels du nouveau DataFrame.

**Questions :**
- Que se passe-t-il pour Bob, Diana et Fatima ?
- Pourquoi Pandas ne les traite-t-il pas comme une addition avec zéro ?
- Comment pourrait-on obtenir une valeur pour tous les employés ?

## 6. Défi supplémentaire

Sans utiliser de boucle Python :

1. Ajoutez une colonne `Salaire après augmentation (€)` correspondant à une augmentation de 7 % du salaire mensuel.
2. Calculez la différence totale de coût annuel pour l'entreprise si tous les employés reçoivent cette augmentation, en tenant compte d'une majoration employeur de 25 %, mais sans modifier les primes.
3. Vérifiez que le DataFrame contient toujours six employés.

**Contraintes générales :**
- Utiliser Pandas.
- Ne pas utiliser de boucle `for` pour les calculs.
- Ne pas utiliser `loc`, `iloc`, `groupby` ou les filtres booléens.
- Ne pas modifier les données initiales fournies.
