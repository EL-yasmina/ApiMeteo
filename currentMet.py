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
    # Chemin complet du fichier JSON
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "w") as json_file:
        # Écrit les données au format JSON avec indentation
        json.dump(donnees, json_file, indent=4)


def get_weather_data(city, api_key):
    """
    Récupère les données météorologiques actuelles pour une ville donnée.

    Args:
        city (str): Le nom de la ville pour laquelle récupérer les données météorologiques actue
        api_key (str): La clé API pour accéder aux données de l'API WeatherAPI.

    Returns:
        la température, la température ressentie et les conditions météorologiques actuelles.
    """
    # URL de l'API pour les données météorologiques actuelles
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    # Faire une requête GET pour obtenir les données météorologiques actuelles
    response = requests.get(url)
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Convertir la réponse en format JSON
        data = response.json()
        # Récupérer la température, la température ressentie et les conditions météorologiques actu
        temperature = data["current"]["temp_c"]
        temperature = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        conditions = data["current"]["condition"]["text"]
        # Sauvegarder les données météorologiques actuelles dans un fichier JSON
        sauvegarder_donneesCurrent_json(data, "currentMet.json", "dataa")
        # Retourner les données météorologiques actuelles
        return temperature, feels_like, conditions
    else:
        # Si la requête échoue, afficher un message d'erreur avec le code de statut
        print(f"Erreur lors de la récupération des données météorologiques: {response.status_code}")
        # Retourner None pour chaque donnée météorologique actuelle
        return None, None, None

# Clé API pour accéder aux données de l'API WeatherAPI
api_key = "61064c6295144de9b63101812242904"
city = "lille"

# Appel à la fonction get_weather_data
temperature, feels_like, conditions = get_weather_data(city, api_key)

# Afficher les données météorologiques actuelles
print(f"Les conditions météorologiques actuelles à {city}:")
print(f"Température: {temperature:.1f}°C")
print(f"Ressentie: {feels_like:.1f}°C")
print(f"Conditions: {conditions}")
