# main.py
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
from services.reservation_service import (
    create_reservation,
    cancel_reservation
)


def show_menu():
    """Display system menu."""
    print("\nReservation System")
    print("1. Create Hotel")
    print("2. Modify Hotel")
    print("3. Display Hotel")
    print("4. Delete Hotel")
    print("5. Create Customer")
    print("6. Modify Customer")
    print("7. Display Customer")
    print("8. Delete Customer")
    print("9. Create Reservation")
    print("10. Cancel Reservation")
    print("0. Exit")


def main():
    """Main program loop."""
    while True:
        show_menu()
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

        elif option == "5":
            create_customer(
                int(input("Customer ID: ")),
                input("Name: ")
            )

        elif option == "6":
            modify_customer(
                int(input("Customer ID: ")),
                input("New Name: ")
            )

        elif option == "7":
            display_customer(int(input("Customer ID: ")))

        elif option == "8":
            delete_customer(int(input("Customer ID: ")))

        elif option == "9":
            create_reservation(
                int(input("Reservation ID: ")),
                int(input("Customer ID: ")),
                int(input("Hotel ID: "))
            )

        elif option == "10":
            cancel_reservation(int(input("Reservation ID: ")))

        elif option == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()