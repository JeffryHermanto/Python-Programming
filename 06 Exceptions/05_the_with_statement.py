# The With Statement

try:
    with open("app.py") as file:
        print("File opened.")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except FileNotFoundError:
    print('No such file or directory')
else:
    print("No exceptions were thrown.")
