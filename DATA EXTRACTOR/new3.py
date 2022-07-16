import json

import requests


# from logging import exception

# from main import BuddhaAir




# a = BuddhaAir()
# a.get_logged_in_session()

f = open("data.json","r")
customers = json.load(f)

for i in customers:
    r = requests.get(f"http://127.0.0.1:8000/customers/?customer_name={i['passenger_name']}").json()
    if r['name']==None:
        r = requests.post('http://127.0.0.1:8000/customers/',data=i)