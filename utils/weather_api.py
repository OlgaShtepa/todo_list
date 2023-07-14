import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = "c4b416389c654a7f85f53253230307"
CITY = "Kiev"

def get_weather_data():
    url = BASE_URL + "?key=" + API_KEY + "&q=" + CITY

    try:
        response = requests.get(url).json()
        print(response)
        return response
    except Exception as e:
        print("Error occurred:", e)
        return None

get_weather_data()