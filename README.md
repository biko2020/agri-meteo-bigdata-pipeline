# Agri-Météo Big Data Pipeline

Pipeline ETL (Extract, Transform, Load) scalable pour collecter, traiter et analyser des données **météorologiques** et **agricoles** à grande échelle.  
L'objectif : fournir des insights actionnables pour optimiser les rendements agricoles en fonction des conditions climatiques (température, précipitations, humidité, etc.).

---

## Logique du Pipeline (Vision Métier)

Le projet suit une architecture classique ETL :

1. **Extract** : Collecte automatisée via APIs (OpenWeatherMap, FAO, Copernicus, etc.) et fichiers historiques.
2. **Transform** : Nettoyage, enrichissement et agrégation avec **PySpark** pour traiter de gros volumes de données.
3. **Load** : Stockage optimisé (format Parquet, Delta Lake) et/ou insertion dans une base de données (PostgreSQL, BigQuery…).
4. **Visualisation** : Dashboard interactif (Streamlit, Power BI, Tableau) pour suivre les indicateurs clés.

---

### Dépendances 
Toutes les dépendances sont listées dans `requirements.txt`.
    pyspark>=3.4.0
    pandas>=2.0
    requests>=2.28
    pyyaml>=6.0
    python-dotenv>=1.0
    sqlalchemy>=2.0
    psycopg2-binary>=2.9  

## Structure du Projet

agri-meteo-bigdata-pipeline/
│
├── data/
│   ├── raw/                 # Données brutes
│   ├── processed/           # Données nettoyées
│
├── scripts/
│   ├── extract.py           # Collecte données (API / CSV)
│   ├── transform.py         # Nettoyage & agrégation (PySpark)
│   ├── load.py              # Insertion DB / Parquet
│
├── notebooks/
│   └── exploration.ipynb    # Analyse exploratoire (optionnel)
│
├── dashboard/
│   └── screenshots/         # Images Power BI / Tableau
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── config/
│   └── config.yaml          # Config API / DB
│
├── requirements.txt
├── README.md
└── .gitignore


## Installation
    - git clone https://github.com/biko2020/agri-meteo-bigdata-pipeline.git
    - cd agri-meteo-bigdata-pipeline

## Créer un environnement virtuel (recommandé)

# Linux / macOS
    python -m venv .venv
    source .venv/bin/activate

 # Windows
    python -m venv .venv
    .venv\Scripts\activate


## Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt


## -***- Exécution du projet -***-

 - # Exécution locale simple
    # 1. Collecte des données 
    python scripts/extract.py

    # 2. Transformation (PySpark)
    spark-submit scripts/transform.py

    # 3. Chargement
    python scripts/load.py
    
 - # Exécution Utiliser Docker
    `Lancer l'ensemble des services (Spark + PostgreSQL + Jupyter):`
    docker-compose up -d
    docker exec -it spark-master bash
    spark-submit /app/scripts/transform.py

- # Exécution Utiliser Jupyter Notebook
    jupyter lab notebooks/exploration.ipynb
    `Ou via Docker :`
    docker-compose up jupyter
    http://localhost:8888

---


## 👤 Contact
    **AIT OUFKIR BRAHIM** 
    Email : aitoufkirbrahimab@gmail.com
    🔗 GitHub : https://github.com/biko2020/agri-meteo-bigdata-pipeline