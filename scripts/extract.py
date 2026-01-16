import requests
import pandas as pd
from configparser import ConfigParser

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 33.6,
        "longitude": -7.6,
        "daily": "temperature_2m_max,precipitation_sum",
        "timezone": "Africa/Casablanca"
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "temp_max": data["daily"]["temperature_2m_max"],
        "precipitation": data["daily"]["precipitation_sum"]
    })
    df.to_csv("data/raw/weather.csv", index=False)

if __name__ == "__main__":
    fetch_weather()
