from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# --- SECTION 1 : CONFIGURATION GLOBALE (default_args) ---
# Ces arguments s'appliquent à TOUTES les tâches du DAG par défaut.
default_args = {
    "owner": "airflow",         # Nom du responsable du DAG
    "start_date": datetime(2024, 1, 1), # Date à laquelle le calendrier Airflow a commencé
    "retries": 1,               # Nombre de tentatives automatiques si une tâche échoue
}

# --- SECTION 2 : DÉFINITION DU DAG ---
# C'est ici que l'on définit l'identité et le planning du robot.
with DAG(
    dag_id="agri_meteo_etl",     # L'identifiant unique qui apparaît sur votre interface web
    schedule_interval="@daily",  # AUTOMATISATION : S'exécute seul chaque jour à minuit
    catchup=False,               # Évite de lancer des centaines de jobs pour rattraper 2024 et 2025
    default_args=default_args,   # Applique les paramètres de la section 1
) as dag:

    # --- SECTION 3 : DÉFINITION DES TÄCHES (Tasks) ---

    # Étape A : Extraction (Récupération des données brutes)
    extract = BashOperator(
        task_id="extract_weather",
        # Commande envoyée au conteneur Spark pour lancer le script Python
        bash_command="docker exec spark python3 /app/scripts/extract.py"
    )

    # Étape B : Transformation (Nettoyage et calculs avec Spark)
    transform = BashOperator(
        task_id="transform_weather",
        # Utilisation de spark-submit pour traiter les données en masse
        bash_command="docker exec spark spark-submit /app/scripts/transform.py"
    )

    # Étape C : Chargement (Envoi des résultats finaux vers PostgreSQL)
    load = BashOperator(
        task_id="load_to_postgres",
        # Exécution du script de chargement final
        bash_command="docker exec spark python3 /app/scripts/load.py"
    )

    # --- SECTION 4 : ORCHESTRATION (Le flux) ---
    # Définit l'ordre d'exécution : d'abord extract, PUIS transform, PUIS load
    extract >> transform >> load