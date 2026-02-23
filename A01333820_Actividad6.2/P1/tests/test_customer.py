"""Unit tests for the Customer model."""
import unittest
from models.customer import Customer


class TestCustomer(unittest.TestCase):
    """Unit tests for the Customer model."""

    def test_create(self):
        """Test creating a customer."""
        customer = Customer(1, "John")
        self.assertEqual(customer.name, "John")

    def test_to_dict(self):
        """Test conversion of Customer to dictionary."""
        customer = Customer(1, "John")
        self.assertEqual(customer.to_dict()["customer_id"], 1)