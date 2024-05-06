import requests
import json
import os

def sauvegarder_donneesHisto_json(donnees, nom_fichier, dossier):
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





def get_historical_weather_data(city, api_key, date):
    """
    Récupère les données météorologiques historiques pour une ville donnée à une date donnée.
    Args:
        city (str): Le nom de la ville pour laquelle récupérer les données météorologiques historiques.
        api_key (str): La clé API pour accéder aux données de l'API WeatherAPI.
        date (str): La date pour laquelle récupérer les données historiques (format : "YYYY-MM-DD").
    Returns:
        la température moyenne et les conditions météorologiques pour la date spécifiée.
    """
    # URL de l'API pour les données historiques
    url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={date}"

    # Faire une requête GET pour obtenir les données historiques
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Convertir la réponse en format JSON
        data = response.json()

        # Récupérer la température moyenne et les conditions météorologiques historiques
        temperature = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        conditions = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]

        # Sauvegarder les données historiques dans un fichier JSON
        sauvegarder_donneesHisto_json(data, "history.json", "dataa")

        # Retourner la température moyenne et les conditions météorologiques
        return temperature, conditions
    else:

        print(f"Erreur lors de la récupération des données: {response.status_code}")
        # Retourner None pour chaque donnée météorologique historique
        return None, None

# Clé API pour accéder aux données de l'API WeatherAPI
api_key = "61064c6295144de9b63101812242904"
# Nom de la ville pour laquelle récupérer les données météorologiques historiques
city = "Fes"
# Date pour laquelle récupérer les données historiques
date = "2024-04-05"

# Appeler la fonction pour récupérer les données météorologiques historiques
temperature, conditions = get_historical_weather_data(city, api_key, date)


# Afficher les données météorologiques historiques
print(f"Les conditions météorologiques historiques à {city} le {date}:")
print(f"Température moyenne: {temperature:.1f}°C")
print(f"Conditions: {conditions}")
