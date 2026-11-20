# Exercice SQLAlchemy iris — informations pratiques

- **Énoncé** : `exo_SQLAlchemy.ipynb`.
- L'énoncé mentionne SSMS (SQL Server). Dans ce cours, on utilise **PostgreSQL** : créez la base avec `psql`, pgAdmin ou une requête `CREATE DATABASE`, puis utilisez une chaîne de connexion `postgresql+psycopg://utilisateur:motdepasse@localhost:5432/nom_de_la_base` (chapitre 11).
- **Données** : l'énoncé charge `iris` avec `seaborn.load_dataset`, qui télécharge le fichier. Sans connexion, utilisez la copie locale `donnees/drills/iris.data` (format UCI, sans en-tête : `header=None`).
