import requests
import json
import os

def sauvegarder_donneesCurrent_json(donnees, nom_fichier, dossier):
    """
    Sauvegarde les données dans un fichier JSON.

    Args:
        donnees (dict): Les données à sauvegarder.
        nom_fichier (str): Le nom du fichier JSON de sortie.
    """
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "w") as json_file:
        json.dump(donnees, json_file, indent=4)


def get_weather_data(city, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"


    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        temperature = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        conditions = data["current"]["condition"]["text"]

        sauvegarder_donneesCurrent_json(data, "currentMet.json", "dataa")
        return temperature, feels_like, conditions
    else:

        print(f"Erreur lors de la récupération des données météorologiques: {response.status_code}")
        return None, None, None


api_key = "61064c6295144de9b63101812242904"
city = "lille"

# Appel à la fonction get_weather_data
temperature, feels_like, conditions = get_weather_data(city, api_key)


print(f"Les conditions météorologiques actuelles à {city}:")
print(f"Température: {temperature:.1f}°C")
print(f"Ressentie: {feels_like:.1f}°C")
print(f"Conditions: {conditions}")
