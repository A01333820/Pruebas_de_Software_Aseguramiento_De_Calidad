"""Hotel Model Module"""

class Hotel:
    """Hotel entity."""

    def __init__(self, hotel_id, name, total_rooms):
        """Initialize a new hotel."""
        if total_rooms < 0:
            raise ValueError("Rooms cannot be negative")

        self.hotel_id = hotel_id
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms

    def reserve_room(self):
        """Reserve a room if available."""
        if self.available_rooms <= 0:
            return False
        self.available_rooms -= 1
        return True

    def cancel_reservation(self):
        """Cancel a reservation and free up a room."""
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1

    def to_dict(self):
        """Convert hotel to dictionary."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "total_rooms": self.total_rooms,
            "available_rooms": self.available_rooms
        }

    @staticmethod
    def from_dict(data):
        """Create a Hotel instance from a dictionary."""
        hotel = Hotel(
            data["hotel_id"],
            data["name"],
            data["total_rooms"]
        )
        hotel.available_rooms = data["available_rooms"]
        return hotel
