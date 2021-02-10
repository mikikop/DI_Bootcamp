import requests
import json
from time import sleep

# resp = requests.get("https://api.chucknorris.io/jokes/random")

# data = resp.json()

# print(data['value'])


while True :
	resp2 = requests.get("http://api.open-notify.org/iss-now.json")
	data2 = resp2.json()
	print(data2['iss_position']['latitude'], data2['iss_position']['longitude'])
	sleep(1)