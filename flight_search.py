import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from dotenv import load_dotenv

load_dotenv()

URL_SEARCH = os.getenv("URL_SEARCH")
URL_LOCATION = os.getenv("URL_LOCATION")
API_KEY = os.getenv("API_KEY")
headers = {
    "apikey" : API_KEY
}
tomorrow_date = datetime.now()
delta = relativedelta(months=6)
future_date = (tomorrow_date + delta).strftime("%d/%m/%Y")
delta = relativedelta(days=1)
tomorrow_date = (tomorrow_date+delta).strftime("%d/%m/%Y")


class FlightSearch:
    def __init__(self, start, destination,curr="USD", date_from=tomorrow_date, date_to=future_date):
        self.paramaters = {
            "fly_from" : start,
            "fly_to" : destination,
            "date_from" : date_from,
            "date_to" : date_to,
            "limit" : 10,
            "curr" : curr,
            "flight_type" : "round",
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
        }
    
    def find_flights(self):
        response = requests.get(URL_SEARCH, params=self.paramaters, headers=headers)
        return response.json()

class IATACodes:
    def __init__(self,city):
        self.parameters = {
            "term": city
        }
    
    def get_iata(self):
        response = requests.get(URL_LOCATION, params=self.parameters, headers=headers)
        return response.json()