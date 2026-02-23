"""Reservation Service Module"""
from storage import load_data, save_data
from models.reservation import Reservation

HOTELS_FILE = "data/hotels.json"
CUSTOMERS_FILE = "data/customers.json"
RESERVATIONS_FILE = "data/reservations.json"


def create_reservation(res_id, customer_id, hotel_id):
    """Create a new reservation."""
    hotels = load_data(HOTELS_FILE)
    customers = load_data(CUSTOMERS_FILE)
    reservations = load_data(RESERVATIONS_FILE)

    hotel = next((h for h in hotels if h["hotel_id"] == hotel_id), None)
    customer = next(
        (c for c in customers if c["customer_id"] == customer_id), None)

    if hotel is None:
        print("Hotel not found")
        return

    if customer is None:
        print("Customer not found")
        return

    if hotel["available_rooms"] <= 0:
        print("No rooms available")
        return

    hotel["available_rooms"] -= 1
    reservation = Reservation(res_id, customer_id, hotel_id)

    reservations.append(reservation.to_dict())
    save_data(HOTELS_FILE, hotels)
    save_data(RESERVATIONS_FILE, reservations)


def cancel_reservation(res_id):
    """Cancel an existing reservation."""
    reservations = load_data(RESERVATIONS_FILE)
    hotels = load_data(HOTELS_FILE)

    for r in reservations:
        if r["reservation_id"] == res_id:
            hotel = next(
                (h for h in hotels if h["hotel_id"] == r["hotel_id"]),
                None
            )
            if hotel:
                hotel["available_rooms"] += 1

            reservations.remove(r)
            save_data(HOTELS_FILE, hotels)
            save_data(RESERVATIONS_FILE, reservations)
            return

    print("Reservation not found")
