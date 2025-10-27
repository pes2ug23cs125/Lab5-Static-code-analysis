# Lab5-Static-code-analysis
# Simple Inventory Management System (`inventory_system.py`)

This is a basic Python script demonstrating fundamental static code analysis fixes, file I/O, and inventory management logic.

---

## 🚀 Features

* **Add/Remove Items:** Functions to update stock quantities.
* **Low Stock Check:** Identifies items below a set threshold.
* **Persistence:** Saves and loads inventory data using a JSON file (`inventory.json`).
* **Validated Code:** Cleaned of major bugs, security flaws, and style issues identified by static analysis tools (Pylint, Bandit, Flake8).

---

## 🛠️ Usage

### Prerequisites

You need Python 3.x installed.

### Run the Script

1.  Save the code as `inventory_system.py`.
2.  Run from your terminal:

    ```bash
    python inventory_system.py
    ```

### Inventory Data

The inventory data is stored in the global dictionary `stock_data` and is saved/loaded from `inventory.json`.

---

## ✨ Code Quality Improvements

This code has been improved to resolve critical issues, including:

* **Security:** Removed the dangerous `eval()` function.
* **Bugs:** Fixed the **mutable default argument** issue in `add_item`.
* **Robustness:** Implemented **resource management** (`with open(...)`) and specific **error handling** (`except KeyError`).
* **Style:** Converted to standard **snake\_case** naming and added **docstrings**.