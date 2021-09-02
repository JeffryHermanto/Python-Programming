# Raising Exceptions

def calculate_x_factor(age):
    if age <= 10:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_x_factor(-1)
except ValueError as error:
    print(error)
