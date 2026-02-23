# storage.py
import json
import os


def load_data(filename):
    """Load JSON file safely."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print(f"Invalid data in file: {filename}")
        return []


def save_data(filename, data):
    """Save JSON file safely."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)