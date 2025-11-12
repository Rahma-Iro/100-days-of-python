# 🔐 Day 5 – Password Generator (Python)

## 🧠 Project Overview
This project is a simple **Password Generator** built in Python as part of a beginner learning challenge.  
It allows users to generate secure passwords by combining **letters**, **numbers**, and **symbols** —  
first in an **Easy Mode** (ordered characters), and then in a **Hard Mode** (shuffled characters for extra security).

---

## 🚀 Features
- Generates **random passwords** with customizable length.
- Includes **uppercase and lowercase letters**.
- Supports **numbers (0–9)** and **special symbols** (e.g. `!@#$%&*`).
- Two levels:
  - 🟢 **Easy Mode** – ordered characters (letters → numbers → symbols)
  - 🔵 **Hard Mode** – fully randomized character order
- Simple **command-line interface** for user input.

---

## 🧩 How It Works
1. The program asks:
   - How many letters you want in your password  
   - How many symbols you want  
   - How many numbers you want  
2. It stores all possible characters in lists:
   ```python
   letters = ['a', 'b', ..., 'Z']
   numbers = ['0', '1', ..., '9']
   symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
