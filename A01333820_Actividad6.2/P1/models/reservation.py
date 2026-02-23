"""Reservation Model Module"""


class Reservation:
    """Reservation entity."""

    def __init__(self, reservation_id, customer_id, hotel_id):
        """Initialize a new reservation."""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convert reservation to dictionary."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id
        }

    @staticmethod
    def from_dict(data):
        """Create a Reservation instance from a dictionary."""
        return Reservation(
            data["reservation_id"],
            data["customer_id"],
            data["hotel_id"]
        )
