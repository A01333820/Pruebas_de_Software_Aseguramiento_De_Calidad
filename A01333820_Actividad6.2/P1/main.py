""" main.py """
from services.hotel_service import (
    create_hotel,
    modify_hotel,
    display_hotel,
    delete_hotel
)
from services.customer_service import (
    create_customer,
    modify_customer,
    display_customer,
    delete_customer
)
from services.reservation_services import (
    create_reservation,
    cancel_reservation
)


def hotel_menu():
    """Hotel submenu."""
    while True:
        print("\n--- Hotel Menu ---")
        print("1. Create Hotel")
        print("2. Modify Hotel")
        print("3. Display Hotel")
        print("4. Delete Hotel")
        print("0. Back")

        option = input("Select option: ")

        if option == "1":
            create_hotel(
                int(input("Hotel ID: ")),
                input("Name: "),
                int(input("Total Rooms: "))
            )

        elif option == "2":
            modify_hotel(
                int(input("Hotel ID: ")),
                input("New Name: "),
                int(input("New Rooms: "))
            )

        elif option == "3":
            display_hotel(int(input("Hotel ID: ")))

        elif option == "4":
            delete_hotel(int(input("Hotel ID: ")))

        elif option == "0":
            break

        else:
            print("Invalid option")


def customer_menu():
    """Customer submenu."""
    while True:
        print("\n--- Customer Menu ---")
        print("1. Create Customer")
        print("2. Modify Customer")
        print("3. Display Customer")
        print("4. Delete Customer")
        print("0. Back")

        option = input("Select option: ")

        if option == "1":
            create_customer(
                int(input("Customer ID: ")),
                input("Name: ")
            )

        elif option == "2":
            modify_customer(
                int(input("Customer ID: ")),
                input("New Name: ")
            )

        elif option == "3":
            display_customer(int(input("Customer ID: ")))

        elif option == "4":
            delete_customer(int(input("Customer ID: ")))

        elif option == "0":
            break

        else:
            print("Invalid option")


def reservation_menu():
    """Reservation submenu."""
    while True:
        print("\n--- Reservation Menu ---")
        print("1. Create Reservation")
        print("2. Cancel Reservation")
        print("0. Back")

        option = input("Select option: ")

        if option == "1":
            create_reservation(
                int(input("Reservation ID: ")),
                int(input("Customer ID: ")),
                int(input("Hotel ID: "))
            )

        elif option == "2":
            cancel_reservation(int(input("Reservation ID: ")))

        elif option == "0":
            break

        else:
            print("Invalid option")


def main():
    """Main system menu."""
    while True:
        print("\n===== Reservation System =====")
        print("1. Hotels")
        print("2. Customers")
        print("3. Reservations")
        print("0. Exit")

        option = input("Select option: ")

        if option == "1":
            hotel_menu()

        elif option == "2":
            customer_menu()

        elif option == "3":
            reservation_menu()

        elif option == "0":
            print("Exiting system...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
