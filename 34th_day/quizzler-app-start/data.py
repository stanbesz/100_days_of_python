import requests

requests_params = {
    "amount":10,
    "type":"boolean"
}

requests_data = requests.get(url="https://opentdb.com/api.php",params=requests_params)
requests_data.raise_for_status()
question_data = requests_data.json()["results"]