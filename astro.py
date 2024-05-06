import requests
import json
import os

def sauvegarder_heures_soleil(data, nom_fichier):
    """
    Sauvegarde les heures de lever et de coucher du soleil dans un fichier JSON.

    Args:
        data (dict): Les données à sauvegarder.
        nom_fichier (str): Le nom du fichier JSON de sortie.
    """
    chemin = os.path.join("dataa", nom_fichier)  # Chemin du fichier dans le dossier "dataa"
    with open(chemin, "w") as json_file:
        json.dump(data, json_file, indent=4)

def get_sunrise_sunset(city, api_key):
    """
    Récupère l'heure du lever et du coucher du soleil pour une ville donnée.

    Args:
        city (str): Le nom de la ville pour laquelle récupérer les données.
        api_key (str): La clé d'API pour accéder au service d'astronomie.

    Returns:
        str: L'heure du lever du soleil.
        str: L'heure du coucher du soleil.
    """
    url = f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        astronomy_data = data.get("astronomy", {})
        if astronomy_data:
            sunrise = astronomy_data["astro"]["sunrise"]
            sunset = astronomy_data["astro"]["sunset"]
            # Sauvegarde des données dans un fichier JSON
            sauvegarder_heures_soleil({"sunrise": sunrise, "sunset": sunset}, "sunrise_sunset.json")
            return sunrise, sunset
    else:
        print(f"Erreur lors de la récupération des données astronomiques: {response.status_code}")
        return None, None

# Clé d'API et nom de la ville pour lesquels récupérer les données astronomiques
api_key = "61064c6295144de9b63101812242904"
city = "london"

# Appel à la fonction get_sunrise_sunset pour récupérer les heures de lever et de coucher du soleil
sunrise, sunset = get_sunrise_sunset(city, api_key)

# Affichage des heures de lever et de coucher du soleil si elles sont disponibles
if sunrise is not None:
    print(f"Heure du lever du soleil à {city}: {sunrise}")
    print(f"Heure du coucher du soleil à {city}: {sunset}")