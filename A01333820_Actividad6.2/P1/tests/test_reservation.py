"""Unit tests for the Reservation model."""
import unittest
from models.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Unit tests for the Reservation model."""

    def test_create(self):
        """Test creating a reservation."""
        reservation = Reservation(1, 10, 20)
        self.assertEqual(reservation.customer_id, 10)

    def test_to_dict(self):
        """Test conversion of Reservation to dictionary."""
        reservation = Reservation(1, 10, 20)
        self.assertEqual(reservation.to_dict()["hotel_id"], 20)
