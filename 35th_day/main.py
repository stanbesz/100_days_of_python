import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

OMW_API_KEY = os.environ.get("OMW_API_KEY")

account_sid = os.getenv("TWILLIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

params = {
    "lat":43.856258, # currently in Sofia
    "lon":18.413076,
    "appid":OMW_API_KEY,
    "cnt":4,
}

response_time = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=params)

response_time.raise_for_status()
print("Code: ", response_time.status_code)
weather_data = response_time.json()
bring_umbrella = False

for weather_instance in weather_data["list"]:
    time = weather_instance["dt_txt"]
    weather_cond:list = []
    
    for weather in weather_instance["weather"]:
        if weather["id"] < 700:
            bring_umbrella = True
        weather_cond.append(weather["id"])
    print(f"At: {time}, it will be: {weather_cond} -> {'Bring an umbrella!' if bring_umbrella else 'You dont need an umbrella!'}")

if bring_umbrella:
    client = Client(account_sid,TWILIO_AUTH_TOKEN)
    message = client.messages.create(body="It's going to rain today. Please bring an umbrella1 ☔",
                                     from_="+12209460604",
                                     to="+359895411678")
    
    print(message.sid)