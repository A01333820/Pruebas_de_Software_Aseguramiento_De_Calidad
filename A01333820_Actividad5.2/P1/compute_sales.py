"""compute_sales.py - Compute total sales from product and sales data"""
import json
import sys
import time


def load_products(filename):
    """Load products and return dictionary {product_name: price}"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            products = json.load(file)

        product_dict = {}
        for product in products:
            name = product["title"]
            price = product["price"]
            product_dict[name] = price

        return product_dict

    except FileNotFoundError:
        print(f"Error: Product file not found -> {filename}")
        sys.exit(1)


def process_sales(product_dict, sales_filename):
    """Process sales file and compute total"""
    total = 0
    errors = []

    try:
        with open(sales_filename, "r", encoding="utf-8") as file:
            sales = json.load(file)

        for sale in sales:
            product_name = sale["Product"]
            quantity = sale["Quantity"]

            # Validar cantidad negativa
            if quantity < 0:
                errors.append(
                    f"Negative quantity detected -> "
                    f"Product: {product_name}, Quantity: {quantity}"
                )
                continue

            # Validar producto inexistente
            if product_name not in product_dict:
                errors.append(
                    f"Product not found in catalog -> {product_name}"
                )
                continue

            price = product_dict[product_name]
            total += price * quantity

        return total, errors

    except FileNotFoundError:
        print(f"Error: Sales file not found -> {sales_filename}")
        sys.exit(1)

def main():
    """Main function to execute the sales computation"""
    if len(sys.argv) != 3:
        print("Usage: python sales.py ProductList.json Sales.json")
        sys.exit(1)

    start_time = time.time()

    product_file = sys.argv[1]
    sales_file = sys.argv[2]

    products = load_products(product_file)
    total, errors = process_sales(products, sales_file)

    elapsed = time.time() - start_time

    print("Total Sales:", total)
    print("Execution Time:", f"{elapsed:.6f} seconds")

    if errors:
        print("\nErrors detected:")
        for error in errors:
            print(error)

    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        file.write(f"Total Sales: {total}\n")
        file.write(f"Execution Time: {elapsed:.6f} seconds\n")

        if errors:
            file.write("\nErrors detected:\n")
            for error in errors:
                file.write(error + "\n")


if __name__ == "__main__":
    main()
