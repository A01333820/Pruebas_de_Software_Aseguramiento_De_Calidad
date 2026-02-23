"""Customer Model Module"""


class Customer:
    """Customer entity."""

    def __init__(self, customer_id, name):
        """Initialize a new customer."""
        self.customer_id = customer_id
        self.name = name

    def to_dict(self):
        """Convert customer to dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name
        }

    @staticmethod
    def from_dict(data):
        """Create a Customer instance from a dictionary."""
        return Customer(
            data["customer_id"],
            data["name"]
        )
