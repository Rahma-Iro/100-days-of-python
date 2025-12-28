# ☕ Day 16 – Intermediate Object-Oriented Programming (OOP)

This project is part of **Day 16** of Angela Yu’s **100 Days of Python** Bootcamp.  
The focus of this day is on **Intermediate Object-Oriented Programming (OOP)** and applying OOP concepts by **refactoring the Coffee Machine project from Day 15 into an object-oriented design**.

---

## 📌 Learning Objectives

On Day 16, I learned and practiced:

- Why **Object-Oriented Programming (OOP)** is important
- How OOP works in Python
- Creating **classes and objects**
- Using **attributes** and **methods**
- Constructing objects and accessing their data
- Installing and using **Python packages from PyPI**
- Modifying object attributes and calling methods
- Applying OOP concepts in a real-world project

---

## 🧠 Why Object-Oriented Programming?

In earlier days, the Coffee Machine was built using **procedural programming**, relying on:
- Global variables
- Independent functions
- Dictionaries for data storage

While functional, this approach becomes harder to maintain as projects grow.

**OOP solves this by:**
- Grouping related data and behavior together
- Making code more modular and readable
- Allowing reuse and scalability
- Modeling real-world systems more naturally

---

## 🏗️ Project Overview: OOP Coffee Machine

The Coffee Machine was rebuilt using **four main classes**, each with a clear responsibility.

### 1️⃣ MenuItem Class
Represents a single drink.

**Attributes:**
- `name` (str): Name of the drink
- `cost` (float): Price of the drink
- `ingredients` (dict): Required ingredients and quantities

---

### 2️⃣ Menu Class
Represents the menu containing all available drinks.

**Methods:**
- `get_items()` → Returns all available drinks as a string  
  _(e.g. `"espresso/latte/cappuccino"`)_
- `find_drink(order_name)` → Returns a `MenuItem` object if found, otherwise `None`

---

### 3️⃣ CoffeeMaker Class
Handles resources and coffee preparation.

**Methods:**
- `report()` → Prints remaining resources
- `is_resource_sufficient(drink)` → Checks if ingredients are enough
- `make_coffee(order)` → Deducts ingredients and makes the coffee

---

### 4️⃣ MoneyMachine Class
Handles payment and profit tracking.

**Methods:**
- `report()` → Prints current profit
- `make_payment(cost)` → Processes coins and validates payment

---

## 🔄 Program Flow

1. Display available drinks from the menu  
2. Ask the user for input  
3. Handle special commands:
   - `off` → turns off the machine
   - `report` → prints resource and money reports
4. Find the selected drink
5. Check if resources are sufficient
6. Process payment
7. Make the coffee if all checks pass

---

# 📦 Python Packages (PyPI)

This day also introduced **PyPI (Python Package Index)** and how to install external packages using `pip`.

### Example:
```bash
pip install prettytable
