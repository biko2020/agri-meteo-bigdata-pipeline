# 🌾 Agri-Meteo Big Data Pipeline

Pipeline **Big Data / ETL (Extract, Transform, Load)** pour collecter, nettoyer, transformer et analyser des données **météorologiques** (extensible aux données agricoles), afin de produire des **indicateurs décisionnels exploitables**.

🎯 **Objectif du projet**  
Démontrer la mise en place d’un pipeline de données **scalable, reproductible et orienté production**, prêt pour des **cas d’usage professionnels et missions freelance** (Data Engineering / Big Data / BI).

---

## 🎯 Vision Métier

Dans de nombreux secteurs (agriculture, énergie, environnement, logistique), les données météo sont :
- dispersées (APIs, fichiers CSV),
- volumineuses et hétérogènes,
- difficiles à exploiter directement par les décideurs.

Ce projet fournit une **chaîne de traitement complète** permettant de transformer ces données brutes en **KPI clairs et exploitables**, prêts à être visualisés dans des outils de Business Intelligence.

---

## 🧠 Logique du Pipeline (ETL)

Le projet suit une architecture ETL classique, orientée production :

1. **Extract**
   - Collecte automatisée des données météo via API publique
   - Stockage des données brutes (*raw data*)

2. **Transform**
   - Nettoyage des données (formats, valeurs manquantes)
   - Agrégation et calcul d’indicateurs avec **PySpark**

3. **Load**
   - Stockage optimisé au format **Parquet**
   - Insertion dans une base **PostgreSQL**

4. **Exploitation**
   - Données prêtes pour la visualisation (Power BI, Tableau, etc.)

---

## 🏗️ Architecture globale

API / CSV
↓
Python (Extract)
↓
PySpark (Transform)
↓
Parquet / PostgreSQL
↓
Dashboard BI


---

## 🛠️ Technologies utilisées

- **Python**
- **PySpark**
- **Pandas**
- **SQL / PostgreSQL**
- **Docker & Docker Compose**
- **Power BI / Tableau** (visualisation)

---

## 📊 Exemples d’indicateurs produits

- Température moyenne par période
- Cumul des précipitations
- Tendances saisonnières
- Données prêtes pour analyses métier ou corrélations ultérieures

---

## 📦 Dépendances

Toutes les dépendances Python sont listées dans `requirements.txt` :
pyspark
pandas
requests
pyyaml
sqlalchemy
psycopg2-binary


---

## 📁 Structure du projet

agri-meteo-bigdata-pipeline/
│
├── data/
│ ├── raw/ # Données brutes
│ └── processed/ # Données transformées
│
├── scripts/
│ ├── extract.py # Extraction des données
│ ├── transform.py # Nettoyage & agrégation (PySpark)
│ └── load.py # Chargement vers DB / Parquet
│
├── notebooks/
│ └── exploration.ipynb # Analyse exploratoire
│
├── dashboard/
│ └── screenshots/ # Captures des dashboards
│
├── docker/
│ ├── Dockerfile
│ └── docker-compose.yml
│
├── config/
│ └── config.yaml # Configuration API / DB
│
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Installation (Docker – recommandé)

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/biko2020/agri-meteo-bigdata-pipeline.git
cd agri-meteo-bigdata-pipeline

### 2️⃣ Lancer l’environnement complet avec Docker
docker compose up -d
docker ps


▶️ Exécution du pipeline avec Docker
   # Accéder au conteneur Spark
   docker exec -it spark-master bash 

   # 1. Extraction
   python /app/scripts/extract.py

   # 2. Transformation (PySpark)
   spark-submit /app/scripts/transform.py

   # 3. Chargement
   python /app/scripts/load.py


###  Cas d’usage 

* Ce pipeline est directement applicable à des missions telles que :

* création de pipelines ETL,

* traitement de données volumineuses,

* migration CSV / Excel vers bases de données,

* préparation de données pour dashboards BI,

* projets Data Engineering / Big Data.


### Contact

** AIT OUFKIR BRAHIM
** Data Engineer / Big Data Developer

   - Email : aitoufkirbrahimab@gmail.com
   - GitHub : https://github.com/biko2020/agri-meteo-bigdata-pipeline