import requests
from datetime import datetime
import smtplib
import time
#----------------------Logic------------------------------
def check_location_iss_near(iss_longitude,iss_latitude,local_long,local_lat):
    if local_long-5<=iss_longitude<=local_long+5 and local_lat-5<=iss_latitude<=local_lat+5:
        print("In position!")
        return True
    else:
        print("ISS Long: ",iss_longitude,"ISS Lat: ",iss_latitude,"Local long: ",local_long,"Local lat: ",local_lat)
        return False

def currently_dark(hour_now,sunrise_time,sunset_time):
    if hour_now > sunset_time or hour_now<sunrise_time:
        print("it is dark now!")
        return True
    else:
        print("Still sunny!")
        return False
#----------------------ISS---------------------------------
response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")

response_iss.raise_for_status()

data = response_iss.json()
print(data)
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = data["iss_position"]
print(iss_position) 

#----------------------Location-----------------------------
MY_LAT = 42.697708
MY_LNG = 23.321867

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}
# response = requests.get(f"https://api.sunrise-sunset.org/json?lat={parameters['lat']}&lng={parameters['lng']}")
response_dark = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response_dark.raise_for_status()

data = response_dark.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)

time_now = datetime.now()

print(time_now.hour)
check_time = check_location_iss_near(iss_longitude=longitude,iss_latitude=latitude,local_lat=MY_LAT,local_long=MY_LNG)
check_dark = currently_dark(time_now.hour,sunrise_time=sunrise,sunset_time=sunset)

while True:
    time.sleep(60)
    if check_dark and check_time:
        print("Look up!")
        my_email = "stanbesz503@gmail.com"
        password = "ifel zjzp drno kdhk"
        with smtplib.SMTP("smtp.gmail.com") as connection: # Same as the file reading/writing
            connection.starttls() #make connection secure
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs="stanbesz503@gmail.com",msg=f"Subject: Look up! Iss Station in the nightsky! \n\n ISS Long:{longitude} ISS Lat: {latitude} \n Your Lat: {MY_LAT} Long:{MY_LNG}")