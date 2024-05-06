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
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "w") as json_file:
        json.dump(donnees, json_file, indent=4)

def get_match_avenir(api_key,city):
    url = f"http://api.weatherapi.com/v1/sports.json?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        match = data['football'][0]  # Accédez au premier match dans la liste
        stade = match['stadium']
        tournoi = match['tournament']
        date = match['start']
        match_name = match['match']

        match_data = {
            "stade": stade,
            "tournament": tournoi,
            "date": date,
            "match": match_name
        }
        
        sauvegarder_donnees_json(match_data, "match.json", "dataa")  # Sauvegarde les données du match dans un fichier JSON

        return stade, tournoi, date, match_name

    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return None, None, None, None

api_key = "61064c6295144de9b63101812242904"
city = "london"

stade, tournoi, date, match = get_match_avenir(api_key,city)

if stade is not None:
    print(f"match à venir à {stade}:")
    print(f"¤ Stade: {stade}")
    print(f"¤ Tournament: {tournoi}")
    print(f"¤ date de match: {date}")
    print(f"¤ Match: {match}")
else:
    print("Aucun match à venir trouvé.")
