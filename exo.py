import pandas as pd
import numpy as np

df_employes = pd.DataFrame({
    "nom": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fatima"],
    "departement": ["IT", "RH", "IT", "Marketing", "IT", "RH"],
    "salaire_mensuel": [3200, 2800, 3800, 3000, 4200, 3100],
    "anciennete": [4, 2, 6, 3, 8, 5]
})

print(df_employes)

# Affichez le nombre de lignes et de colonnes.
print(df_employes.shape)


# Affichez les noms des colonnes.
print(df_employes.columns)


# Affichez les types de données de chaque colonne.
print(df_employes.dtypes)


# Affichez les index du DataFrame.
print(df_employes.index)


# Récupérez uniquement la colonne Salaire mensuel (€) dans une variable salaires.
salaires = df_employes["salaire_mensuel"]
print(salaires)


# Salaire annuel (€) : salaire mensuel multiplié par 12.
df_employes["salaire_annuel"] = df_employes["salaire_mensuel"] * 12
print(df_employes)


# Prime (€) : prime annuelle de 500 € par année d'ancienneté.
df_employes["prime"] = df_employes["anciennete"] * 500
print(df_employes)


# Rémunération totale (€) : salaire annuel augmenté de la prime.
df_employes["remuneration_totale"] = df_employes["salaire_annuel"] + df_employes["prime"]
print(df_employes)


# Coût employeur (€) : rémunération totale augmentée de 25 %.
df_employes["cout_employeur"] = df_employes["remuneration_totale"] * 1.25
print(df_employes)


# Calculez le salaire mensuel moyen.
salaire_mensuel_moyen = salaires.mean()
# print(salaire_mensuel_moyen)


# Trouvez le salaire mensuel le plus élevé et le plus faible.
# print("Max : ", salaires.max())
# print("Min : ", salaires.min())


# Calculez le coût employeur total annuel de l'entreprise.
cout_total = df_employes["cout_employeur"].sum()
# print(cout_total)

# Calculez la différence de salaire mensuel entre chaque employé et le salaire moyen.



# Ajoutez cette différence au DataFrame dans une colonne Écart moyenne (€).
df_employes["ecart_moyen"] = df_employes["salaire_mensuel"].sub(salaire_mensuel_moyen)
# df_employes["ecart_moyen"] = df_employes["salaire_mensuel"] - salaire_mensuel_moyen
# print(df_employes)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Créez un nouveau DataFrame, à partir de df_employes, dont les index sont les noms des employés, sans modifier le DataFrame original.
df_index = df_employes.set_index('nom')
print(df_index)


# Affichez ses index.
print(df_index.index)


# Récupérez la colonne des salaires mensuels.
salaires_index = df_index["salaire_mensuel"]


# Créez une Series contenant les valeurs suivantes, avec les index correspondants :
bonus = pd.Series({
    "Alice": 100,
    "Charlie": 200,
    "Ethan": 300
})


# Additionnez cette Series à la colonne des salaires mensuels du nouveau DataFrame.
res = salaires_index.add(bonus, fill_value=0)
print(res)


df_employes["salaire_apres_augmentation"] = df_employes["salaire_mensuel"] * 1.07

augmentation_mensuel = df_employes["salaire_apres_augmentation"] - df_employes["salaire_mensuel"]
print(augmentation_mensuel)

surcout = (augmentation_mensuel * 12 * 1.25).sum()

print(surcout)

assert df_employes.shape[0] == 6

print(df_employes.shape[0])
