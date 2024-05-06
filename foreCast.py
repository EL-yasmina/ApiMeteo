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
    # Chemin complet du fichier JSON
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "w") as json_file:
        # Écrit les données au format JSON avec indentation
        json.dump(donnees, json_file, indent=4)



def get_weather_forecast(city, api_key, days):
    """
    Récupère les données de prévision météorologique pour une ville donnée.
    Args:
        city (str): Le nom de la ville pour laquelle récupérer les données de prévision.
        api_key (str): La clé API pour accéder aux données de l'API WeatherAPI.
        days (int): Le nombre de jours de prévision à récupérer.
    Returns:
        list: Une liste contenant les données de prévision météorologique pour chaque jour.
    """
    # URL de base de l'API de prévision météorologique
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    # Paramètres de la requête GET
    params = {
        "key": api_key,
        "q": city,
        "days": days
    }
    # Faire une requête GET pour obtenir les données de prévision
    response = requests.get(base_url, params=params)
    # Convertir la réponse en format JSON
    data = response.json()

    # Vérifier si les données de prévision sont présentes dans la réponse
    if 'forecast' in data:

        # Récupérer les données de prévision
        forecast_data = data['forecast']['forecastday']

        # Sauvegarder les données de prévision dans un fichier JSON
        sauvegarder_donneesforeCast_json(data, "foreCast.json", "dataa")
        # Retourner les données de prévision pour chaque jou
        return forecast_data
    else:
        print("Erreur: Impossible de récupérer les données de prévision.")
        # Retourner une liste vide si les données de prévision ne sont pas disponibles
        return []

# Clé API pour accéder aux données de l'API WeatherAPI
api_key = '61064c6295144de9b63101812242904'
city = 'Paris'
# Nombre de jours de prévision à récupérer
days = 2

# Appeler la fonction pour récupérer les données de prévision
forecast_data = get_weather_forecast(city, api_key, days)

# Parcourir les données de prévision pour chaque jour
for forecast in forecast_data:
    date = forecast['date']
    avg_temp_c = forecast['day']['avgtemp_c']
    condition_text = forecast['day']['condition']['text']
    
    # Afficher les informations de prévision pour chaque jour
    print("Date:", date)
    print("Température moyenne:", avg_temp_c, "°C")
    print("Conditions météorologiques:", condition_text)
    print()
