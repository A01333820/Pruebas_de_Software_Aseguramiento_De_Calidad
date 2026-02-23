"""Hotel Service Module"""
from storage import load_data, save_data
from models.hotel import Hotel

HOTELS_FILE = "data/hotels.json"


def create_hotel(hotel_id, name, rooms):
    """Create a new hotel."""
    hotels = load_data(HOTELS_FILE)

    if any(h["hotel_id"] == hotel_id for h in hotels):
        print("Hotel already exists")
        return

    hotel = Hotel(hotel_id, name, rooms)
    hotels.append(hotel.to_dict())
    save_data(HOTELS_FILE, hotels)


def modify_hotel(hotel_id, new_name=None, new_rooms=None):
    """Modify an existing hotel's details."""
    hotels = load_data(HOTELS_FILE)

    for h in hotels:
        if h["hotel_id"] == hotel_id:
            if new_name:
                h["name"] = new_name
            if new_rooms is not None:
                h["total_rooms"] = new_rooms
            save_data(HOTELS_FILE, hotels)
            return

    print("Hotel not found")


def display_hotel(hotel_id):
    """"Display hotel details."""
    hotels = load_data(HOTELS_FILE)

    for h in hotels:
        if h["hotel_id"] == hotel_id:
            print(h)
            return

    print("Hotel not found")


def delete_hotel(hotel_id):
    """Delete a hotel."""
    hotels = load_data(HOTELS_FILE)
    updated = [h for h in hotels if h["hotel_id"] != hotel_id]
    save_data(HOTELS_FILE, updated)
