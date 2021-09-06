# Command-line Arguments

import sys

basePath = "09 Python Standard Library"

# print(sys.argv)

if len(sys.argv) == 1:
    print(
        f"USAGE: python3 \"{basePath}/16_command_line_arguments.py\" <password>")
else:
    password = sys.argv[1]
    print("Password", password)
