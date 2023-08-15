# sample.py

import requests
from tut9.myapp.dice import roll_dice

def guess_number(num):
    result = roll_dice()
    if result == num:
        return "you  won"
    else:
        return "you lost"
    

def get_ip():
    response = requests.get("http://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']

    

    