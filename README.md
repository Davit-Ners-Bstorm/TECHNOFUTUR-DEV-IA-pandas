# Pandas pour l'IA — formation de 2 jours

Cours complet sur Pandas 3 pour développeurs IA : diaporama, notebooks de démonstration, exercices, corrections et données. Tout s'exécute localement avec Python 3.15.

## Installation

Prérequis : [uv](https://docs.astral.sh/uv/) **récent** (préparé avec uv 0.11) (`uv --version` ; mise à jour : `uv self update`).

```bash
cd formation-pandas
uv sync
```

`uv sync` installe Python 3.15 si nécessaire (fichier `.python-version`), crée l'environnement `.venv` et installe les dépendances figées dans `uv.lock` : pandas 3.1, NumPy 2.5, pyarrow, SQLAlchemy 2, psycopg 3, openpyxl, lxml, requests, matplotlib, seaborn, JupyterLab.

Python 3.15 est récent : la quasi-totalité des paquets fournit des roues précompilées. PyYAML (dépendance indirecte de JupyterLab) est compilé à l'installation. Si cette étape échoue :
- macOS : `xcode-select --install` ;
- Linux : installer `build-essential` (ou l'équivalent) ;
- Windows : installer les « Microsoft C++ Build Tools ».

## Lancer le cours

```bash
uv run jupyter lab
```

Ouvrir `cours/00_introduction.ipynb`. Les notebooks utilisent des chemins relatifs (`../donnees/...`) : les ouvrir depuis leur dossier, comme le fait JupyterLab par défaut.

Le diaporama est dans `slides/` (PowerPoint et PDF).

## Base de données (chapitre 11, approfondissement A3, exercice SQLAlchemy)

Les notebooks se connectent à PostgreSQL avec, par défaut :

```
postgresql+psycopg://postgres:postgres@localhost:5432/formation_pandas
```

1. Installer PostgreSQL (installeur officiel, Postgres.app, ou Docker : `docker run -d --name pg -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:16`).
2. Créer la base : `createdb -U postgres formation_pandas` (ou `CREATE DATABASE formation_pandas;`).
3. Si l'utilisateur ou le mot de passe diffère, définir `DATABASE_URL` avant de lancer JupyterLab :

```bash
# macOS / Linux
export DATABASE_URL="postgresql+psycopg://utilisateur:motdepasse@localhost:5432/formation_pandas"
# Windows PowerShell
$env:DATABASE_URL = "postgresql+psycopg://utilisateur:motdepasse@localhost:5432/formation_pandas"
```

Sans serveur PostgreSQL, les notebooks du cours basculent automatiquement sur une base SQLite locale (`sorties/formation.db`).

## Sans connexion Internet

- Chapitre 11 : si l'API Open-Meteo n'est pas joignable, une réponse d'exemple locale est utilisée (`donnees/api/`).
- Exercice API météo : définir `FORMATION_HORS_LIGNE=1` pour que les corrections utilisent des réponses simulées (`corrections/bstorm/pandas3/04_call_api/hors_ligne.py`).

## Organisation

```
formation-pandas/
├── slides/            diaporama (PowerPoint, PDF)
├── cours/             un notebook par chapitre (00 à 12) et approfondissements (A1 à A3)
├── exercices/
│   ├── bstorm/        exercices Bstorm d'origine (JO, Sakila, SQLAlchemy, API météo, chunk processing)
│   ├── drills/        exercices d'entraînement : originaux (anglais) et traductions françaises
│   ├── supplementaires/  exercices courts propres au cours (S01 à S12)
│   └── README.md      correspondance exercices / chapitres
├── corrections/
│   ├── bstorm/        originales (inchangées) et versions Pandas 3 avec journal des modifications
│   ├── drills/        originales et versions Pandas 3 avec journal
│   └── supplementaires/
├── donnees/           toutes les données (provenance : donnees/SOURCES.md)
├── annexes/           aide-mémoire Pandas / SQL / NumPy, compléments, sujets historiques non exécutables
├── formateur/         guide formateur, notebooks exécutés, supports théoriques d'origine
├── sorties/           fichiers produits par les notebooks (créé à l'exécution, ignoré par Git)
├── pyproject.toml     dépendances
└── uv.lock            versions figées
```

## Programme

| Chapitre | Contenu |
|---|---|
| 0 | Pourquoi Pandas : tableaux, jeux de données, DataFrame, Series, place dans un projet d'IA |
| 1 | La Series : index, types, alignement, valeurs manquantes |
| 2 | Le DataFrame : construction, types, attributs, opérations |
| 3 | Importer, exporter, découvrir : CSV, Excel, JSON, `info`, `describe` |
| 4 | Sélectionner, filtrer, trier : `loc`, `iloc`, masques, `query` |
| 5 | Nettoyer : doublons, manquants, texte, types, dates, Copy-on-Write |
| 6 | Statistiques et agrégations |
| 7 | GroupBy et tableaux croisés |
| 8 | Jointures et concaténation |
| 9 | Restructurer : `melt`, `pivot`, `explode`, `json_normalize`, `get_dummies` |
| 10 | `map`, `apply` et vectorisation |
| 11 | Pandas connecté : SQLAlchemy et PostgreSQL, API web, pages HTML |
| 12 | Synthèse : préparer un jeu de données pour un modèle |
| A1 | Séries temporelles |
| A2 | Gros volumes : lecture par blocs |
| A3 | SQL avancé avec SQLAlchemy |

## Versions

Vérifié avec Python 3.15.0b4, pandas 3.1.1, NumPy 2.5.5, SQLAlchemy 2.1.9, psycopg 3.3.9 et PostgreSQL 16. Les corrections d'origine écrites pour Pandas 1 et 2 sont conservées sans modification ; les versions adaptées à Pandas 3 documentent chaque changement dans un journal.
