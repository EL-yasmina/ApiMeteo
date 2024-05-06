import requests
import json
import os

def sauvegarder_donneesforeCast_json(donnees, nom_fichier, dossier):
    """
    Sauvegarde les données dans un fichier JSON.

    Args:
        donnees (dict): Les données à sauvegarder.
        nom_fichier (str): Le nom du fichier JSON de sortie.
    """
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "w") as json_file:
        json.dump(donnees, json_file, indent=4)



def get_weather_forecast(city, api_key, days):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": city,
        "days": days
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'forecast' in data:
        forecast_data = data['forecast']['forecastday']

        sauvegarder_donneesforeCast_json(data, "foreCast.json", "dataa")
        return forecast_data
    else:
        print("Erreur: Impossible de récupérer les données de prévision.")
        return []


api_key = '61064c6295144de9b63101812242904'
city = 'Paris'
days = 2

forecast_data = get_weather_forecast(city, api_key, days)

for forecast in forecast_data:
    date = forecast['date']
    avg_temp_c = forecast['day']['avgtemp_c']
    condition_text = forecast['day']['condition']['text']

    print("Date:", date)
    print("Température moyenne:", avg_temp_c, "°C")
    print("Conditions météorologiques:", condition_text)
    print()
