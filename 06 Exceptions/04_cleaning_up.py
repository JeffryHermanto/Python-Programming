# Cleaning Up

try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except FileNotFoundError:
    print('No such file or directory')
else:
    print("No exceptions were thrown.")
finally:
    print("Finally")
    if not FileNotFoundError:
        file.close()
