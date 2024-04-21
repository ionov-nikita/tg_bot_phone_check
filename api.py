import os

import requests
from dotenv import load_dotenv


PHONE_LOOKUP_API = "https://api.veriphone.io/v2/verify"
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_info(phone_number):
    try:
        if len(phone_number) not in (11, 12):
            raise Exception
        if phone_number.startswith("+"):
            phone_number = int(phone_number[1:])
        else:
            phone_number = int(phone_number)
        params = {"phone": phone_number, "key": API_KEY}

        response = requests.get(PHONE_LOOKUP_API, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return False
    except Exception as e:
        return e
