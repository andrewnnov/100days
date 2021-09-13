import requests

api_key = ""

MY_LAT = 56.326790
MY_LONG = 44.005989


OWM_Endpoint = f"https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()
print(data)





