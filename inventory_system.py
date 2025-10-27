"""
A simple inventory management system for tracking stock data.
This module demonstrates basic file I/O, error handling, and code style improvements.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Adds an item and its quantity to the inventory, and logs the action.
    Ensures that 'qty' is an integer before proceeding.
    """
    if logs is None:
        logs = []

    if not item or not isinstance(qty, int):
        print(f"Warning: Failed to add item. Item must be non-empty and "
              f"quantity must be an integer. Received item={item}, qty={qty}")
        return
        
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """Removes a quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Silently fail if item is not in stock
        pass

def get_qty(item):
    """Returns the quantity of a specific item in stock."""
    return stock_data.get(item)

def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file."""
    global stock_data # W0603: Necessary to reassign the global variable
    try:
        with open(file, "r", encoding='utf-8') as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        # This is a safe way to handle the file not existing on first run
        pass

def save_data(file="inventory.json"):
    """Saves inventory data to a JSON file."""
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(stock_data))

def print_data():
    """Prints a report of all items and their quantities."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_low_items(threshold=5):
    """Returns a list of items with quantity below the given threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    """Main execution function for the inventory system."""
    add_item("apple", 10)
    add_item("banana", -2)
    # Fixed: Changed invalid types to valid integer types to prevent TypeError
    add_item("nuts", 10)
    remove_item("apple", 3)
    remove_item("orange", 1)
    
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()