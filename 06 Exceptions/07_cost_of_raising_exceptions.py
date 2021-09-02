# Cost of Raising Exceptions

from timeit import timeit

code1 = """
def calculate_x_factor(age):
    if age <= 10:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_x_factor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_x_factor(age):
    if age <= 10:
        return None
    return 10 / age


xfactor = calculate_x_factor(-1)
if xfactor == None:
    pass
"""

print("First Code =", timeit(code1, number=10000))
print("Second Code =", timeit(code2, number=10000))
