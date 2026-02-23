class Hotel:
    """Hotel entity."""

    def __init__(self, hotel_id, name, total_rooms):
        if total_rooms < 0:
            raise ValueError("Rooms cannot be negative")

        self.hotel_id = hotel_id
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms

    def reserve_room(self):
        if self.available_rooms <= 0:
            return False
        self.available_rooms -= 1
        return True

    def cancel_reservation(self):
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1

    def to_dict(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "total_rooms": self.total_rooms,
            "available_rooms": self.available_rooms
        }

    @staticmethod
    def from_dict(data):
        hotel = Hotel(
            data["hotel_id"],
            data["name"],
            data["total_rooms"]
        )
        hotel.available_rooms = data["available_rooms"]
        return hotel