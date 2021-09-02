# Scope
# - Local
# - Global

message = "x"


def greet(name):
    message = "a"
    print(message)


greet("Jeffry")


def send_email(name):
    message = "b"
    print(message)


send_email("Jeffry")


print(message)


def send_message(name):
    global message
    message = "c"
    print(message)


send_message("Jeffry")
