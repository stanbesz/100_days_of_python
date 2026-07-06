import requests
import datetime
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/bakeboard-hot-100/"
FALLBACK_DATE = "2026-02-28"  # known-good date, used if the requested chart isn't available

def date_logic():

    input_date = input("For which date are you interested in the Billboard 100? Format required YYYY-MM-DD:\n")
    date_info = list(map(int,input_date.strip().split('-')))
    date_obj = datetime.date(year=date_info[0],month=date_info[1],day=date_info[2])

    # weekday(): Monday=0 ... Sunday=6, so Saturday=5
    days_until_saturday = 5 - date_obj.weekday()
    saturday_date = date_obj + datetime.timedelta(days=days_until_saturday)

    return saturday_date


def collect_bakeboard_data(playlist_date):

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
    
    valid_date_flag = False
    
    try:
        response = requests.get(URL + playlist_date.isoformat(), headers=header)
        response.raise_for_status()
        valid_date_flag = True
    except requests.exceptions.RequestException as e:
        print(f"Couldn't fetch chart for {playlist_date.isoformat()} ({e}). Falling back to {FALLBACK_DATE}.")
        response = requests.get(URL + FALLBACK_DATE, headers=header)
        response.raise_for_status()
        valid_date_flag = False

    return [valid_date_flag, response]

def create_song_map(bakeboard_response):

    soup = BeautifulSoup(bakeboard_response.text,"html.parser")
    song_lists = soup.find_all("div",class_="chart-entry__info")

    song_maps:dict = {}

    for song in song_lists:
        song_maps[song.h3.string]=song.span.string

    return song_maps
