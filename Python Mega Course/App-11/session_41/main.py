import pandas  # type: ignore

df = pandas.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        return availability == "yes"

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        return f"Reservation confirmed for {self.customer_name} at hotel ID {self.hotel_object.name}."

print(df)
hotel_ID = input("Enter a hotel id: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    print("Hotel is available")
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
    
else:
    print("Hotel is not available")
