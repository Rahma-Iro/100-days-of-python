# ☕ Day 15 – Coffee Machine Program (100 Days of Python)

This project is part of **Day 15** of the *100 Days of Python* challenge by Angela Yu.  
The goal of this day was to build a **command-line coffee machine simulation** that follows real-world logic and constraints.

The program allows users to order drinks, insert coins, receive change, and tracks available resources and profit.

---

## 📌 Project Overview

The Coffee Machine program simulates how a real coffee machine works. It can:

- Serve **espresso**, **latte**, and **cappuccino**
- Check if enough resources are available before making a drink
- Accept and process coins
- Refund money if payment is insufficient
- Give change when too much money is inserted
- Keep track of profit
- Display a report of available resources
- Shut down using a secret command

---

## ☕ Available Drinks

| Drink        | Water | Milk | Coffee | Cost ($) |
|-------------|------|------|--------|----------|
| Espresso    | 50ml | 0ml  | 18g    | 1.50     |
| Latte       | 200ml| 150ml| 24g    | 2.50     |
| Cappuccino  | 250ml| 100ml| 24g    | 3.00     |

---

## 🧠 Key Concepts Practiced

- Dictionaries and nested dictionaries
- Functions with parameters and return values
- Global vs local scope
- Conditional logic (`if`, `elif`, `else`)
- While loops
- Input validation
- Resource management
- Modular programming
- Real-world problem decomposition

---

## ⚙️ Program Features Explained

### 1️⃣ User Prompt
The program continuously asks:
What would you like? (espresso/latte/cappuccino):

yaml
Copy code
until the machine is turned off.

---

### 2️⃣ Turning Off the Machine
Typing:
off

yaml
Copy code
will stop the program completely.  
(This is meant for maintainers only.)

---

### 3️⃣ Printing a Report
Typing:
report

diff
Copy code
will display:
- Remaining water
- Remaining milk
- Remaining coffee
- Total profit earned

Example:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

yaml
Copy code

---

### 4️⃣ Resource Check
Before making a drink, the machine checks:
- Is there enough water?
- Is there enough milk?
- Is there enough coffee?

If not, the program prints:
Sorry there is not enough <resource>.

yaml
Copy code

---

### 5️⃣ Coin Processing
The user inserts coins:
- Quarters ($0.25)
- Dimes ($0.10)
- Nickels ($0.05)
- Pennies ($0.01)

The total value is calculated and returned.

---

### 6️⃣ Transaction Validation
- If **not enough money** → refund
- If **exact amount** → proceed
- If **too much money** → give change

Change is rounded to **2 decimal places**.

---

### 7️⃣ Making Coffee
If everything is successful:
- Resources are deducted
- Profit increases
- The drink is served

Message shown:
Here is your latte ☕️. Enjoy!

yaml
Copy code

---

## 🗂️ Code Structure

| Function Name | Purpose |
|--------------|--------|
| `is_resource_sufficient()` | Checks if enough ingredients exist |
| `process_coins()` | Calculates total money inserted |
| `is_transaction_successful()` | Validates payment |
| `make_coffee()` | Deducts ingredients and serves drink |

---

## ▶️ How to Run the Program

1. Make sure Python is installed
2. Save the file as `main.py`
3. Run:
```bash
python main.py
🎯 What I Learned
How to break a large problem into smaller functions

How real-world systems handle money and resources

Why clean structure and readable functions matter

How to think like a programmer, not just write code