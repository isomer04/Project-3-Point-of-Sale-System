
# Point of Sale System

This project is a Point of Sale (POS) system implemented in Python. The GUI of the system is created using the guizero module. The system allows the user to place orders for food and drinks, and prints a ticket with the order details and total price.

## Requirements

* Python 3.6+
* guizero module
* MySQL

## Usage

1. Clone the repository.
2. Install the guizero module: `pip install guizero`
3. Run the `main.py` file using Python: `python main.py`
4. Select the food item and quantity from the drop-down menus, and click "Add Food".
5. Select the drink item and quantity from the drop-down menus, and click "Add Drink".
6. Once all items are added, click "Submit Order" to print the ticket.

## Code Overview

The `main` function defines three nested functions: `food_order`, `drink_order`, and `submit_order`. The `food_order` and `drink_order` functions add the selected items and quantities to a list, and calculate the total price of the order. The `submit_order` function prints the ticket with the order details and total price.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
