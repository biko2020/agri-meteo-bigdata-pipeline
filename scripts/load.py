import pandas as pd
from sqlalchemy import create_engine

# Créer une connexion SQLAlchemy
engine = create_engine("postgresql://postgres:postgres@postgres:5432/agri_db")

# Lire le fichier Parquet
df = pd.read_parquet("/app/data/processed/weather.parquet")

# Charger dans PostgreSQL
df.to_sql("weather_kpi", engine, if_exists="replace", index=False)

print(f"✓ {len(df)} lignes chargées dans PostgreSQL")

# Fermer la connexion
engine.dispose()