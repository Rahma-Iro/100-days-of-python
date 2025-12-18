# 100 Days of Python - Day 12: Scope and Number Guessing Game

## Topics Covered

- **Local vs Global Scope:** 
  - Local variables exist only inside the function where they are defined.
  - Global variables exist throughout the program and can be accessed anywhere.
  
- **Namespaces:** 
  - Python uses namespaces to manage variable names and their scopes.
  
- **Modifying Global Variables:** 
  - You can modify global variables inside a function using the `global` keyword, or return a new value.
  
- **Constants in Python:**
  - Variables like `PI` or URLs are considered constants by convention (all uppercase letters).

- **Prime Number Checker:**
  - Learned how to check if a number is prime using loops and conditional statements.

## Final Project: Number Guessing Game

- The game generates a random number.
- The player guesses the number.
- The program provides feedback whether the guess is too high, too low, or correct.
- The game tracks the number of attempts.

## Example Code Snippets

```python
# Prime Number Checker
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Modifying Global Variable
enemies = 1
def increase_enemies(enemy):
    return enemy + 1
enemies = increase_enemies(enemies)

# Constants
PI = 3.14159
GOOGLE_URL = "https://www.google.com"
