import requests
import json
import os



def sauvegarder_donnees_json(donnees, nom_fichier,dossier):
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

def get_match_avenir(api_key,city):
    """
    Récupère les données sur le prochain match de football en utilisant une API de météo sportive.

    Args:
        api_key (str): Clé API pour accéder aux données de l'API de météo sportive.
        city (str): Nom de la ville pour laquelle récupérer les données du match.

    Returns:
        les détails du match (stade, tournoi, date, match_name).
    """
    # URL de l'API
    url = f"http://api.weatherapi.com/v1/sports.json?key={api_key}&q={city}"
    # Faire une requête GET pour obtenir les données
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Convertir la réponse en format JSON
        data = response.json()
        # Accédez au premier match dans la liste
        match = data['football'][0]  
        stade = match['stadium']
        tournoi = match['tournament']
        date = match['start']
        match_name = match['match']

        # Créer un dictionnaire avec les détails du match
        match_data = {
            "stade": stade,
            "tournament": tournoi,
            "date": date,
            "match": match_name
        }

        # Appeler la fonction pour sauvegarder les données
        sauvegarder_donnees_json(match_data, "match.json", "dataa") 
        # Retourner les détails du match
        return stade, tournoi, date, match_name

    else:
        # Si la requête échoue, afficher un message d'erreur avec le code de statu
        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return None, None, None, None
# Clé API pour accéder aux données de l'API de météo sportive
api_key = "61064c6295144de9b63101812242904"
# Nom de la ville pour laquelle récupérer les données du match
city = "london"

# Appeler la fonction pour récupérer les détails du match à venir
stade, tournoi, date, match = get_match_avenir(api_key,city)

# Si des détails de match sont retournés
if stade is not None:
    print(f"match à venir à {stade}:")
    print(f"¤ Stade: {stade}")
    print(f"¤ Tournament: {tournoi}")
    print(f"¤ date de match: {date}")
    print(f"¤ Match: {match}")
else:
    # Afficher un message indiquant qu'aucun match n'a été trouvé
    print("Aucun match à venir trouvé.")
