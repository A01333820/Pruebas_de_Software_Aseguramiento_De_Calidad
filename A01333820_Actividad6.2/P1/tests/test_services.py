"""Unit tests for hotel services."""
import unittest
import os

from services.hotel_service import (
    create_hotel,
    modify_hotel,
    display_hotel,
    delete_hotel
)

from storage import load_data

TEST_FILE = "data/hotels.json"


class TestServices(unittest.TestCase):

    def setUp(self):
        """Reset test file before each test."""
        with open(TEST_FILE, "w", encoding="utf-8") as file:
            file.write("[]")

    # ------------------------
    # CREATE TESTS
    # ------------------------

    def test_create_hotel(self):
        create_hotel(1, "Hotel Test", 5)
        data = load_data(TEST_FILE)
        self.assertEqual(len(data), 1)

    def test_duplicate_hotel(self):
        create_hotel(1, "Hotel Test", 5)
        create_hotel(1, "Hotel Test", 5)
        data = load_data(TEST_FILE)
        self.assertEqual(len(data), 1)

    # ------------------------
    # MODIFY TESTS
    # ------------------------

    def test_modify_name(self):
        create_hotel(2, "Hotel A", 10)
        modify_hotel(2, new_name="Hotel B")
        data = load_data(TEST_FILE)
        self.assertEqual(data[0]["name"], "Hotel B")

    def test_modify_rooms(self):
        create_hotel(3, "Hotel C", 8)
        modify_hotel(3, new_rooms=20)
        data = load_data(TEST_FILE)
        self.assertEqual(data[0]["total_rooms"], 20)

    def test_modify_not_found(self):
        modify_hotel(999, new_name="X")  # should execute "Hotel not found"

    # ------------------------
    # DISPLAY TESTS
    # ------------------------

    def test_display_existing(self):
        create_hotel(4, "Hotel D", 12)
        display_hotel(4)  # should print hotel

    def test_display_not_found(self):
        display_hotel(999)  # should print "Hotel not found"

    # ------------------------
    # DELETE TESTS
    # ------------------------

    def test_delete_existing(self):
        create_hotel(5, "Hotel E", 6)
        delete_hotel(5)
        data = load_data(TEST_FILE)
        self.assertEqual(len(data), 0)

    def test_delete_not_found(self):
        delete_hotel(999)  # should still save without crashing


if __name__ == "__main__":
    unittest.main()