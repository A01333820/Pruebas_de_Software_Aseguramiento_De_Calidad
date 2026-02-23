import unittest
from models.hotel import Hotel


class TestHotelModel(unittest.TestCase):

    def test_reserve(self):
        hotel = Hotel(1, "Test", 2)
        self.assertTrue(hotel.reserve_room())

    def test_no_rooms(self):
        hotel = Hotel(1, "Test", 0)
        self.assertFalse(hotel.reserve_room())

    def test_cancel(self):
        hotel = Hotel(1, "Test", 1)
        hotel.reserve_room()
        hotel.cancel_reservation()
        self.assertEqual(hotel.available_rooms, 1)


if __name__ == "__main__":
    unittest.main()