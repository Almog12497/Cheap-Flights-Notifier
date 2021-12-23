
class FlightData:
    def __init__(self,data):
        self.data = data

    def cheapest_flight(self):
        self.city = self.data["data"][0]["cityTo"]
        self.prices = [int(price["price"]) for price in self.data["data"]]
        self.price = min(self.prices)
        return f'{self.city}: ${self.price}'

    def format_sms(self):
        self.index = self.prices.index(self.price)
        self.flight =  self.data["data"][self.index]
        self.arrival = f'{self.flight["cityTo"]}-{self.flight["cityCodeTo"]}'
        self.dep = f'{self.flight["cityFrom"]}-{self.flight["cityCodeFrom"]}'
        self.dep_date = self.flight["route"][0]['local_departure'].split("T")[0]
        self.arrival_date = self.flight["route"][1]['local_departure'].split("T")[0]
        return f"Low price alert! Only ${self.price} to fly from {self.dep} to {self.arrival}, from {self.dep_date} to {self.arrival_date}.\n"

    def format_email(self):
        return self.format_sms() + self.flight["deep_link"]
