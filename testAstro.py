import pytest
from astro import get_sunrise_sunset

def test_get_sunrise_sunset():
    # cas de test 1 vérifie si la fonction retourne des valeurs non nulles pour une ville valide
    api_key = "61064c6295144de9b63101812242904"
    city = "london"
    sunrise, sunset = get_sunrise_sunset(city, api_key)
    assert sunrise is not None
    assert sunset is not None

    # cas de test 2 vérifie si la fonction retourne None pour une clé d'API invalide ou une ville inexist
    api_key = "invalid_key"
    city = "nonexistent_city"
    sunrise, sunset = get_sunrise_sunset(city, api_key)
    assert sunrise is None
    assert sunset is None