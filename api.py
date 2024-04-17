import requests
from config import API_KEY


PHONE_LOOKUP_API = "https://api.veriphone.io/v2/verify"


def get_info(phone_number):
    try:
        if len(phone_number) != 11:
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
