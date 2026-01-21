# 🌾 Agri-Meteo Big Data Pipeline

Pipeline **Big Data / ETL** pour collecter, transformer et analyser des données météorologiques, produisant des **indicateurs décisionnels exploitables** pour l'agriculture, l'énergie et l'environnement.

---

## 🎯 Vision Métier

Les données météorologiques sont souvent dispersées, volumineuses et difficiles à exploiter. Ce projet fournit une **chaîne de traitement complète** transformant les données brutes en **KPI clairs**, prêts pour la Business Intelligence.

---

## 🧠 Architecture ETL

```
API / CSV
    ↓
Python (Extract)
    ↓
PySpark (Transform)
    ↓
Parquet / PostgreSQL
    ↓
Dashboard BI
```

**1. Extract** – Collecte automatisée via API  
**2. Transform** – Nettoyage et agrégation avec PySpark  
**3. Load** – Stockage optimisé (Parquet + PostgreSQL)  
**4. Exploitation** – Visualisation BI (Power BI, Tableau)

---

## 🛠️ Stack Technique

- **Python** – Orchestration
- **PySpark** – Traitement distribué
- **PostgreSQL** – Base de données
- **Docker & Docker Compose** – Déploiement
- **Parquet** – Format optimisé
- **Power BI / Tableau** – Visualisation

---

## 📊 Indicateurs Produits

- Température moyenne par période
- Cumul des précipitations
- Tendances saisonnières
- Corrélations météo-agricoles

---

## 📁 Structure du Projet

```
agri-meteo-bigdata-pipeline/
│
├── data/
│   ├── raw/              # Données brutes
│   └── processed/        # Données transformées
│
├── airflow/
│   ├── dags/
│   │   └── agri_meteo_etl.py
│   ├── logs/
│   ├── plugins/
│   └── docker-compose.airflow.yml

│
├── scripts/
│   ├── extract.py        # Extraction API
│   ├── transform.py      # Transformation 
│   └── load.py           # Chargement vers DB / Parquet
│
├── notebooks/
│   └── exploration.ipynb # Analyse exploratoire
│
├── dashboard/
│   └── screenshots/      # Visualisations
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml        # Spark + Postgres métier
│   ├── docker-compose.airflow.yml
│
├── config/
│   └── config.yaml       # Configuration
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🐳 Installation avec Docker (Recommandé)

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/biko2020/agri-meteo-bigdata-pipeline.git
cd agri-meteo-bigdata-pipeline
```

### 2️⃣ Démarrer l'environnement

```bash
docker compose up -d
docker ps
```

### 3️⃣ Exécuter le pipeline

```bash
# Accéder au conteneur Spark
docker exec -it spark bash

# 1. Extraction
python3 /app/scripts/extract.py

# 2. Transformation et Nettoyage et calculs massifs  (PySpark)
spark-submit /app/scripts/transform.py

# 3. Chargement
python3 /app/scripts/load.py
```

### 4️⃣ Accéder à Spark UI

```
http://localhost:8081
```

---

## 💼 Cas d'Usage Professionnels

Ce pipeline est directement applicable pour :

- Création de pipelines ETL production
- Traitement de données volumineuses (Big Data)
- Migration CSV/Excel vers bases de données
- Préparation de données pour dashboards BI
- Projets Data Engineering / Data Science

---

## 📦 Dépendances Python

```
pyspark
pandas
requests
pyyaml
sqlalchemy
psycopg2-binary
```

---

##  Contact

**AIT OUFKIR BRAHIM**  
Data Engineer / Big Data Developer

-  Email : aitoufkirbrahimab@gmail.com
-  GitHub : [github.com/biko2020](https://github.com/biko2020/agri-meteo-bigdata-pipeline)
