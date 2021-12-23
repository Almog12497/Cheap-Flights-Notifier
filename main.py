#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch, IATACodes
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager


START = "TLV"

# flight = FlightSearch("TLV","TYO","1000")
# print(flight.find_flights())

#Get IATACode
# sheet = DataManager()
# data = sheet.get_rows()
# cities = [city["city"] for city in data["prices"]]

# for i,city in enumerate(cities):
#     code = IATACodes(city)
#     code = code.get_iata()["locations"][0]["code"]
#     data["prices"][i]["iataCode"] = code

# print(sheet.update_rows(data))



sheet = DataManager()
data = sheet.get_rows("prices")
codes = [city["iataCode"] for city in data ["prices"]]
thresholds = [city["lowestPrice"] for city in data ["prices"]]

#Get users
users = DataManager()
users_data = users.get_rows("users")
emails = [email["email"] for email in users_data["users"]]

for i,code in enumerate(codes):
    flight = FlightSearch(start=START,destination=code)
    flights_data = (flight.find_flights())
    if flights_data != []:
        format = FlightData(flights_data)
        cheapest_flight_string = format.cheapest_flight()
        print(cheapest_flight_string)
        if thresholds[i] > int(cheapest_flight_string.split("$")[1]):
            for email in emails:
                notification = NotificationManager(format.format_email())
                notification.send_email(email)

