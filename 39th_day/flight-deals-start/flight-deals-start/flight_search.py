import time
import requests
from data_manager import DataManager
from pprint import pprint
from dotenv import load_dotenv
from datetime import datetime, timedelta
from urllib.error import HTTPError
import os

load_dotenv()

AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_SECRET_TOKEN = os.getenv("AMADEUS_SECRET_TOKEN")
AMADEUS_AUTH_ENDPOINT = os.getenv("AMADEUS_AUTH_ENDPOINT")
AMADEUS_TEST_ENDPOINT = os.getenv("AMADEUS_TEST_ENDPOINT")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    _api_key = ""
    _api_secret = ""
    _token = ""

    def __init__(self):
        self._api_key = AMADEUS_API_KEY
        self._api_secret = AMADEUS_SECRET_TOKEN
        self._token = self._get_new_token()
        pass

    def _get_new_token(self):
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': AMADEUS_API_KEY,
            'client_secret': AMADEUS_SECRET_TOKEN
        }
        response = requests.post(url=AMADEUS_AUTH_ENDPOINT, headers=header, data=body)
        response.raise_for_status()

        print(f"Your token is: {response.json()['access_token']}")
        print(f"The security token expires in: {response.json()['expires_in']}")
        return response.json()["access_token"]
    
    def get_iata_names(self,flight_sheet_info_manager):

        flight_data = flight_sheet_info_manager.get_flight_data()
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            "Authorization": f"Bearer {self._token}",

        }
        for row in flight_data:
            city = row["city"]
            params = {
                "keyword":city,
            }
            iataCode = requests.get(url=f"{AMADEUS_TEST_ENDPOINT}/reference-data/locations/cities",headers=header,params=params)
            try:
                iataCode.raise_for_status()
                row['iataCode'] = iataCode.json()["data"][0]["iataCode"]
            except HTTPError:
                row['iataCode'] = "N/A"

        return flight_data
        
    pass