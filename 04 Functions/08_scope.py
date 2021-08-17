# Scope
# - Local
# - Global

message = "x"


def greet(name):
    message = "a"
    print(message)


greet("Jeffry")


def sendEmail(name):
    message = "b"
    print(message)


sendEmail("Jeffry")


print(message)


def sendMessage(name):
    global message
    message = "c"
    print(message)


sendMessage("Jeffry")
