"""Unit tests for the Hotel model."""
import unittest
from models.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Unit tests for the Hotel model."""

    def test_create_valid(self):
        """Test creating a hotel with valid data."""
        hotel = Hotel(1, "Test", 5)
        self.assertEqual(hotel.available_rooms, 5)

    def test_negative_rooms(self):
        """Test creating a hotel with negative rooms."""
        with self.assertRaises(ValueError):
            Hotel(1, "Test", -1)

    def test_reserve_success(self):
        """Test reserving a room successfully."""
        hotel = Hotel(1, "Test", 1)
        self.assertTrue(hotel.reserve_room())

    def test_reserve_fail(self):
        """Test reserving a room when none are available."""
        hotel = Hotel(1, "Test", 0)
        self.assertFalse(hotel.reserve_room())

    def test_cancel(self):
        """Test canceling a reservation."""
        hotel = Hotel(1, "Test", 1)
        hotel.reserve_room()
        hotel.cancel_reservation()
        self.assertEqual(hotel.available_rooms, 1)

if __name__ == "__main__":
    unittest.main()
