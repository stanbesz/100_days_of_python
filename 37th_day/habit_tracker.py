import requests
from datetime import datetime

PIXEL_USERNAME = "saleksan"
PIXEL_TOKEN = "scoobydoobiedoojijklajklljkvjkhhjkjkhl"
GRAPH_ID = "graphfloat"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXEL_TOKEN,
    "username":PIXEL_USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(pixela_endpoint,json=user_params)
# print(response.text)

graph_config = {
    "id":GRAPH_ID,
    "name":"Coding practice",
    "unit":"minutes/seconds",
    "type":"float",
    "color":"ajisai",
    "timezone":"Europe/Sofia",
}

headers = {"X-USER-TOKEN":PIXEL_TOKEN}

graph_endpoint = f"{pixela_endpoint}/{PIXEL_USERNAME}/graphs"

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print("Response:",response.text)

today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{PIXEL_USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_config = {
    "quantity":"120.34",
}

response = requests.put(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)