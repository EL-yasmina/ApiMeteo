import pytest
from foreCast import get_weather_forecast

def test_get_weather_forecast():
    # Test case 1 vérifie si la fonction retourne le nombre attendu de jours de prévis
    city = "Paris"
    api_key = "61064c6295144de9b63101812242904"
    days = 2
    forecast_data = get_weather_forecast(city, api_key, days)
    assert len(forecast_data) == days

    # Test case 2 vérifie si la fonction retourne une liste vide pour une ville inexistante
    city = "malom"
    forecast_data = get_weather_forecast(city, api_key, days)
    assert forecast_data == []