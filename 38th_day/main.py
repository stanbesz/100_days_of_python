import time
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()

WORKOUT_API_KEY_ID = os.getenv("WORKOUT_API_KEY_ID")
WORKOUT_API_KEY = os.getenv("WORKOUT_API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")

WORKOUT_URL = os.getenv("WORKOUT_URL")
WORKOUT_ENDPOINT = os.getenv("WORKOUT_ENDPOINT")

workout_description = input('Tell me what did you train today: e.g. "lifted weights 45 min", "weight training" / "ran for 30 minutes", "jogged 2 miles": ')

full_endpoint = f"{WORKOUT_URL}{WORKOUT_ENDPOINT}"

params_workout = {
    "query": workout_description,
    "weight_kg": 85,                  
    "height_cm": 183,                 
    "age": 27,                        
    "gender": "male",
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": WORKOUT_API_KEY_ID,
    "x-app-key": WORKOUT_API_KEY,
}

response = requests.post(full_endpoint,headers=headers,json=params_workout) # important Get requsts have params= => this adds to url; post,put and others have json= due to sending the info to the API via their body
response.raise_for_status()

workout_data = response.json()['exercises']

def create_row_entry(json_info):
    time_now = datetime.now()
    date_entry = time_now.strftime("%d/%m/%Y")
    time_entry = time_now.strftime("%H:%M:%S")
    name_exercise = json_info[0]['name'].title()
    duration_exercise = json_info[0]['duration_min']
    calories_exercise = json_info[0]['nf_calories']

    sheety_object = {
        "workout":{
            "date":date_entry,
            "time":time_entry,
            "exercise":name_exercise,
            "duration":duration_exercise,
            "calories":calories_exercise,
        }
    }

    headers = { "Content-Type": "application/json",
               "Authorization": f"Bearer {os.getenv('SHEETY_AUTH_TOKEN')}",}

    response = requests.post(url=SHEETY_ENDPOINT,headers=headers,json=sheety_object)
    response.raise_for_status()
    pass

create_row_entry(workout_data)