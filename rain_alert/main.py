import requests
import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "twil"
TWILIO_AUTH_TOKEN = "twil"


api_key = "3d5b1dfa763a3d3d1c506be6f72d3cc3"

MY_LAT = 56.326790
MY_LONG = 44.005989


OWM_Endpoint = f"https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # account_sid = os.environ[TWILIO_ACCOUNT_SID]
    # auth_token = os.environ[TWILIO_AUTH_TOKEN]
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='TwilPhone',
        to='myPhone'
    )

    print(message.status)