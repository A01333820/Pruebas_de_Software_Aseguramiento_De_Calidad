"""Unit tests for hotel services."""
import unittest
import os
from services.hotel_service import create_hotel
from storage import load_data

TEST_FILE = "data/hotels.json"


class TestServices(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        with open(TEST_FILE, "w", encoding="utf-8") as file:
            file.write("[]")

    def test_create_hotel(self):
        """Test creating a hotel."""
        create_hotel(1, "Hotel Test", 5)
        data = load_data(TEST_FILE)
        self.assertEqual(len(data), 1)

    def test_duplicate_hotel(self):
        """Test creating a hotel with duplicate ID."""
        create_hotel(1, "Hotel Test", 5)
        create_hotel(1, "Hotel Test", 5)
        data = load_data(TEST_FILE)
        self.assertEqual(len(data), 1)
