import requests
import os
import json

def sauvegarder_donneesCurrentComp_json(donnees, nom_fichier, dossier):
    """
    Sauvegarde les données dans un fichier JSON.

    Args:
        donnees (dict): Les données à sauvegarder.
        nom_fichier (str): Le nom du fichier JSON de sortie.
    """
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "w") as json_file:
        json.dump(donnees, json_file, indent=4)

def get_current_weather(city, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        return data
    else:
        print(f"Erreur lors de la récupération des données météorologiques pour {city}: {response.status_code}")
        return None

def compare_weather(cities, api_key):
    weather_data = {}
    for city in cities:
        data = get_current_weather(city, api_key)
        if data:
            weather_data[city] = {
                "temperature": data["current"]["temp_c"],
                "conditions": data["current"]["condition"]["text"]
            }
            sauvegarder_donneesCurrentComp_json(weather_data, "compare.json", "dataa")
    return weather_data

# Remplacez "YOUR_API_KEY" par votre clé API WeatherAPI
api_key = "61064c6295144de9b63101812242904"

# Liste des villes à comparer
cities_to_compare = ["Paris", "London", "New York"]

# Comparaison des conditions météorologiques
weather_comparison = compare_weather(cities_to_compare, api_key)

# Affichage des résultats
for city, data in weather_comparison.items():
    print(f"Conditions météorologiques actuelles à {city}:")
    print(f"Température: {data['temperature']}°C")
    print(f"Conditions: {data['conditions']}")
    print()
