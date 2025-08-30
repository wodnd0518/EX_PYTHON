import requests
from datetime import datetime

MY_LAT = 36.1456
MY_LONG = 128.3881

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f'sunset: {sunset}')
print(f'sunrise: {sunrise}')

time_now = datetime.now()
print(time_now.hour)