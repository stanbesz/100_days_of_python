import time
import requests
from pprint import pprint
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()

SHEET_FLIGHT_ENDPOINT = os.getenv("SHEET_FLIGHT_ENDPOINT")
SHEET_FLIGHT_AUTH_TOKE = os.getenv("SHEET_FLIGHT_AUTH_TOKE")

class DataManager:

    flight_data_info:dict = {}

    def __init__(self):
        headers = { "Content-Type": "application/json",
               "Authorization": f"Bearer {SHEET_FLIGHT_AUTH_TOKE}",}
        
        response = requests.get(SHEET_FLIGHT_ENDPOINT,headers=headers)  
        response.raise_for_status()

        self.flight_data_info = response.json()["prices"]

        pass

    def get_flight_data(self):
        return self.flight_data_info
    
    def update_flight_data(self,new_data):
        self.flight_data_info = new_data

        headers = { "Content-Type": "application/json",
               "Authorization": f"Bearer {SHEET_FLIGHT_AUTH_TOKE}",}
        for row in self.flight_data_info:
            json = {
                "price": {
                    "city":row['city'],
                    'iataCode':row['iataCode'],
                    'id':row['id'],
                    'lowestPrice':row['lowestPrice']
                }
            }

            response = requests.put(f"{SHEET_FLIGHT_ENDPOINT}/{row['id']}",headers=headers,json=json)  
            response.raise_for_status()

            print(response.json())

    pass