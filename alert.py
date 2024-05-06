import requests
import json
import os
import tkinter as tk
from tkinter import simpledialog

api_key = "61064c6295144de9b63101812242904"
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

def recommandation_vetements(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        sauvegarder_donneesCurrent_json(data, "currentMet_"+city+".json", "dataa")
        temperature_celsius = data['current']['temp_c']
        condition = data['current']['condition']['text']
        precipitation_mm = data['current']['precip_mm']
        if temperature_celsius < 10:
            return "Il fait plutôt frais à {} avec {}°C. Tu devrais peut-être envisager de porter quelque chose de chaud !".format(data['location']['name'], temperature_celsius)
        elif temperature_celsius >= 10 and temperature_celsius < 20:
            if precipitation_mm > 0:
                return "Il y a {} à {} et il fait {}°C. Prends un parapluie et peut-être un pull léger !".format(condition, data['location']['name'], temperature_celsius)
            else:
                return "À {} il fait {}°C, un t-shirt et une veste légère pourraient être parfaits pour toi !".format(data['location']['name'], temperature_celsius)
        else:
            if precipitation_mm > 0:
                return "Il pleut à {} et il fait {}°C. N'oublie pas ton parapluie !".format(data['location']['name'], temperature_celsius)
            else:
                return "Il fait chaud à {} avec {}°C. C'est le moment de sortir les shorts et les lunettes de soleil !".format(data['location']['name'], temperature_celsius)
    else:
        return None
# Création de la fenêtre principale
root = tk.Tk()
root.withdraw()  # Masquer la fenêtre principale

# Afficher une boîte de dialogue avec un champ de saisie
user_input = simpledialog.askstring("Meteo ville", "Entrez votre ville ici :")

message = recommandation_vetements(user_input)

# Afficher le texte saisi
if message is not None:
    tk.messagebox.showinfo("Information", message)

else:
    tk.messagebox.showinfo("Information", "Vous êtes sûr que c'est la bonne ville !")

# Fermer la fenêtre
root.destroy()
