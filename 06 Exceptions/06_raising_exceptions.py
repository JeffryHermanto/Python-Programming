# Raising Exceptions

def calculateXfactor(age):
    if age <= 10:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculateXfactor(-1)
except ValueError as error:
    print(error)
