# List Unpacking

numbers = [1, 2, 3]

first, second, third = numbers
print(first)
print(second)
print(third)

print("")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, *other = numbers
print(first)
print(other)
