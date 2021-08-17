# Exercise

def fizzBuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"
    return input


print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))
print(fizzBuzz(7))
