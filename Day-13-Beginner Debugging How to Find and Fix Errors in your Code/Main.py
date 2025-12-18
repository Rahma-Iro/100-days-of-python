from random import randint

# ------------------------------
# 1. Debugging a simple loop
# ------------------------------
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()

# Describe the Problem:
# 1. The for loop counts from 1 to 20.
# 2. It prints "You got it" when i equals 20.
# 3. i starts at 1 and goes up to 20, inclusive.


# ------------------------------
# 2. Reproducing a dice error
# ------------------------------
# Incorrect version: IndexError because randint starts at 1
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])  # ❌ Error

# Correct version: Indexing starts at 0
dice_num = randint(0, 5)
print(f"Dice rolled: {dice_images[dice_num]}")


# ------------------------------
# 3. Play computer and evaluate each line
# ------------------------------
year = int(input("What's your year of birth? "))

if 1980 < year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")


# ------------------------------
# 4. Handling input errors with try/except
# ------------------------------
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You typed an invalid number. Please try again with a numerical value, e.g., 15.")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")
