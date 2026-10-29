# Test Case 1: Burger, Quantity = 2
# Expected Output: Subtotal = ₹240.00, Total = ₹292.00

# Test Case 2: Fries, Quantity = 1, No Coupon
# Expected Output: Subtotal = ₹80.00, GST = ₹4.00,
# Delivery = ₹40.00, Total = ₹124.00

# Test Case 3: Invalid Item = Sushi, Coupon = FREE50
# Expected Output: Item not available, Invalid coupon code

# Test Case 4: Pizza × 2, Fries × 1, Coupon = SAVE10
# Expected Output: Subtotal = ₹580.00, Discount = ₹58.00,
# GST = ₹26.10, Delivery = ₹0.00, Total = ₹548.10
"""
========================================================
              ONLINE FOOD ORDERING SYSTEM
========================================================
Language : Python 3
Features : Menu, Cart, Coupon, GST, Delivery & Billing
========================================================
"""

# -------------------- CONFIGURATION -------------------- 

MENU = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 80,
    "Coke": 40
}

COUPON_CODE = "SAVE10"
DISCOUNT_RATE = 0.10
GST_RATE = 0.05
DELIVERY_CHARGE = 40
FREE_DELIVERY_LIMIT = 300

# Each cart entry stores item name, price and quantity.
cart = []


# -------------------- DISPLAY FUNCTIONS --------------------

def print_line(char="-", width=50):
    print(char * width)


def display_header():
    print("\n")
    print_line("=", 50)
    print("           ONLINE FOOD ORDERING SYSTEM")
    print_line("=", 50)


def display_menu():
    print("\n" + "=" * 50)
    print("                    FOOD MENU")
    print("=" * 50)
    print(f"{'ITEM':<25}{'PRICE':>25}")
    print_line()

    for item, price in MENU.items():
        print(f"{item:<25}{'Rs. ' + format(price, '.2f'):>25}")

    print_line("=")
    print("All prices are in Indian Rupees (INR).")


# -------------------- CART FUNCTIONS -------------------- 

def calculate_subtotal():
    return sum(
        item["price"] * item["quantity"]
        for item in cart
    )


def add_item():
    display_menu()

    item_name = input("\nEnter item name: ").strip().title()

    if item_name not in MENU:
        print("\n[ERROR] Item not available.")
        print("Available items:", ", ".join(MENU.keys()))
        return

    quantity_input = input("Enter quantity: ").strip()

    if not quantity_input.isdigit() or int(quantity_input) <= 0:
        print("\n[ERROR] Quantity must be a positive integer.")
        return

    quantity = int(quantity_input)

    for item in cart:
        if item["name"] == item_name:
            item["quantity"] += quantity
            break
    else:
        cart.append({
            "name": item_name,
            "price": MENU[item_name],
            "quantity": quantity
        })

    print(f"\n[SUCCESS] {item_name} x{quantity} added to cart.")
    print(f"Cart Subtotal: Rs. {calculate_subtotal():.2f}")


def remove_item():
    if not cart:
        print("\n[INFO] Your cart is empty.")
        return

    item_name = input("\nEnter item name to remove: ").strip().title()

    quantity_input = input("Enter quantity to remove: ").strip()

    if not quantity_input.isdigit() or int(quantity_input) <= 0:
        print("\n[ERROR] Enter a valid positive quantity.")
        return

    quantity = int(quantity_input)

    for item in cart:
        if item["name"] == item_name:
            if quantity > item["quantity"]:
                print("\n[ERROR] Quantity exceeds the cart quantity.")
                return

            item["quantity"] -= quantity

            if item["quantity"] == 0:
                cart.remove(item)

            print(f"\n[SUCCESS] {item_name} removed from cart.")
            print(f"Updated Subtotal: Rs. {calculate_subtotal():.2f}")
            return

    print("\n[ERROR] Item not found in your cart.")


def view_cart():
    print("\n" + "=" * 65)
    print("                         YOUR CART")
    print("=" * 65)

    if not cart:
        print("Your cart is currently empty.")
        print("=" * 65)
        return

    print(f"{'ITEM':<18}{'PRICE':>12}{'QTY':>10}{'AMOUNT':>20}")
    print_line("-", 65)

    for item in cart:
        amount = item["price"] * item["quantity"]

        print(
            f"{item['name']:<18}"
            f"{item['price']:>12.2f}"
            f"{item['quantity']:>10}"
            f"{amount:>20.2f}"
        )

    print_line("-", 65)
    print(f"{'SUBTOTAL':>45} Rs. {calculate_subtotal():.2f}")
    print("=" * 65)


# -------------------- COUPON FUNCTION --------------------

def apply_coupon(subtotal, coupon_code):
    coupon_code = coupon_code.strip().upper()

    if not coupon_code:
        return 0.0

    if coupon_code == COUPON_CODE:
        discount = subtotal * DISCOUNT_RATE
        print("\n[SUCCESS] Coupon SAVE10 applied successfully.")
        return discount

    print("\n[ERROR] Invalid coupon code.")
    print("Only SAVE10 is accepted.")
    return 0.0


# -------------------- CHECKOUT & BILLING --------------------

def checkout():
    if not cart:
        print("\n[INFO] Your cart is empty. Add items before checkout.")
        return

    subtotal = calculate_subtotal()

    print("\n" + "=" * 50)
    print("                     CHECKOUT")
    print("=" * 50)

    coupon_code = input(
        "Enter coupon code (press Enter to skip): "
    )

    discount = apply_coupon(subtotal, coupon_code)
    discounted_amount = subtotal - discount

    gst = discounted_amount * GST_RATE

    if subtotal >= FREE_DELIVERY_LIMIT:
        delivery = 0
    else:
        delivery = DELIVERY_CHARGE

    total = discounted_amount + gst + delivery

    # Print the final invoice.
    print("\n")
    print_line("=", 50)
    print("                 FOOD ORDER INVOICE")
    print_line("=", 50)

    print(f"{'ITEM':<18}{'QTY':>6}{'PRICE':>12}{'AMOUNT':>14}")
    print_line("-", 50)

    for item in cart:
        amount = item["price"] * item["quantity"]

        print(
            f"{item['name']:<18}"
            f"{item['quantity']:>6}"
            f"{item['price']:>12.2f}"
            f"{amount:>14.2f}"
        )

    print_line("-", 50)
    print(f"{'Subtotal':<32} Rs. {subtotal:>10.2f}")
    print(f"{'Discount':<32} Rs. {discount:>10.2f}")
    print(f"{'GST (5%)':<32} Rs. {gst:>10.2f}")

    if delivery == 0:
        print(f"{'Delivery':<32} Rs. {delivery:>10.2f} (FREE)")
    else:
        print(f"{'Delivery':<32} Rs. {delivery:>10.2f}")

    print_line("=", 50)
    print(f"{'GRAND TOTAL':<32} Rs. {total:>10.2f}")
    print_line("=", 50)

    print("\n             Thank you for your order!")
    print("              Enjoy your delicious food.")
    print_line("=", 50)

    # Clear the cart after a successful checkout.
    cart.clear()


# -------------------- MAIN APPLICATION --------------------

def main():
    while True:
        display_header()

        print("  1. View Food Menu")
        print("  2. Add Item to Cart")
        print("  3. Remove Item from Cart")
        print("  4. View Shopping Cart")
        print("  5. Checkout & Generate Bill")
        print("  6. Exit Application")

        print_line()
        choice = input("  Select an option (1-6): ").strip()

        if choice == "1":
            display_menu()

        elif choice == "2":
            add_item()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            view_cart()

        elif choice == "5":
            checkout()

        elif choice == "6":
            print("\n" + "=" * 50)
            print("  Thank you for using our food ordering system!")
            print_line("=", 50)
            break

        else:
            print("\n[ERROR] Invalid option. Please select 1 to 6.")

        input("\nPress Enter to continue...")


# -------------------- PROGRAM ENTRY POINT --------------------

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nApplication closed. Thank you!")