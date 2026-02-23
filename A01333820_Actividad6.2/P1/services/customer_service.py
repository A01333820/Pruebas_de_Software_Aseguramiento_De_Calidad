from storage import load_data, save_data
from models.customer import Customer

CUSTOMERS_FILE = "data/customers.json"


def create_customer(customer_id, name):
    customers = load_data(CUSTOMERS_FILE)

    if any(c["customer_id"] == customer_id for c in customers):
        print("Customer already exists")
        return

    customer = Customer(customer_id, name)
    customers.append(customer.to_dict())
    save_data(CUSTOMERS_FILE, customers)


def modify_customer(customer_id, new_name):
    customers = load_data(CUSTOMERS_FILE)

    for c in customers:
        if c["customer_id"] == customer_id:
            c["name"] = new_name
            save_data(CUSTOMERS_FILE, customers)
            return

    print("Customer not found")


def display_customer(customer_id):
    customers = load_data(CUSTOMERS_FILE)

    for c in customers:
        if c["customer_id"] == customer_id:
            print(c)
            return

    print("Customer not found")


def delete_customer(customer_id):
    customers = load_data(CUSTOMERS_FILE)
    updated = [c for c in customers if c["customer_id"] != customer_id]
    save_data(CUSTOMERS_FILE, updated)