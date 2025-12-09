def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGeLa", "YU"))


def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)

def is_leap_year(year):
    if year % 400 == 0:
        return True          # divisible by 400 → leap year
    elif year % 100 == 0:
        return False         # divisible by 100 → not leap year
    elif year % 4 == 0:
        return True          # divisible by 4 → leap year
    else:
        return False
print(is_leap_year(2400))  # True
print(is_leap_year(1989))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2100))  # False

#docstrings
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
