# Online Food Ordering System

A menu-based food ordering application built with **Python 3**. Users
can browse the menu, add or remove items from their cart, apply a
coupon, and generate a final bill.

## Features

-   Display the food menu with prices
-   Add items to the shopping cart
-   Remove items or quantities from the cart
-   View cart items and subtotal
-   Apply the `SAVE10` coupon for a 10% discount
-   Calculate 5% GST
-   Apply a ₹40 delivery charge on orders below ₹300
-   Provide free delivery on orders of ₹300 or more
-   Generate a detailed invoice at checkout
-   Validate item names, quantities, coupons, and menu choices

## Menu

  Item       Price
  -------- -------
  Burger      ₹120
  Pizza       ₹250
  Fries        ₹80
  Coke         ₹40

## Requirements

-   Python 3
-   A terminal or code editor such as VS Code

No external Python libraries are required.

## How to Run

1.  Save the Python code in a file named `food_ordering_system.py`.

2.  Open a terminal in the folder containing the file.

3.  Run:

    ``` bash
    python food_ordering_system.py
    ```

## Coupon and Billing Rules

-   Valid coupon: `SAVE10`
-   Discount: 10% of the subtotal
-   GST: 5% of the discounted amount
-   Delivery: ₹40 when the subtotal is below ₹300
-   Free delivery: subtotal of ₹300 or more

## Sample Test Cases

1.  **Burger × 2** --- Subtotal: ₹240.00; GST: ₹12.00; Delivery: ₹40.00;
    Total: ₹292.00
2.  **Fries × 1, no coupon** --- Subtotal: ₹80.00; GST: ₹4.00; Delivery:
    ₹40.00; Total: ₹124.00
3.  **Invalid item: Sushi, invalid coupon: FREE50** --- Expected
    messages: `Item not available` and `Invalid coupon code`. These
    checks occur in separate steps of the application.
4.  **Pizza × 2 + Fries × 1, coupon SAVE10** --- Subtotal: ₹580.00;
    Discount: ₹58.00; GST: ₹26.10; Delivery: ₹0.00; Total: ₹548.10

## Python Concepts Used

-   Dictionaries and lists
-   Functions
-   Loops and conditional statements
-   User input and output
-   String methods and validation
-   Arithmetic operations
-   Exception handling

## Future Improvements

-   Save order history
-   Add customer details and order IDs
-   Support multiple coupon codes
-   Add a graphical user interface
-   Store menu items and orders in a database

## Author

Created as a Python project for learning and demonstrating basic food
ordering and billing logic.
