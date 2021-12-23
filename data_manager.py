import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_URL = os.getenv("SHEETY_URL")

sheety_headers = {
    "Authorization": os.getenv("SHEETY_HEADER")
}

class DataManager:
    def get_rows(self,sheet):
        response = requests.get(f'{SHEETY_URL}{sheet}',headers = sheety_headers)
        return(response.json())

    def update_rows(self,new_rows):
        for i,new_row in enumerate(new_rows["prices"]):
            paramters = {
                "price" : new_row
            }
            response = requests.put(f"{SHEETY_URL}/{i+2}", json=paramters, headers=sheety_headers)
        return(response.json())
