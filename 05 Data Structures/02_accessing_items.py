# Accessing Items

letters = ["a", "b", "c", "d"]
print(letters[0])
print(letters[-1])

print("")

letters[0] = "A"
print(letters)

print("")

print(letters[0:3])
print(letters[:3])
print(letters[0:])
print(letters[:])
print(letters[::2])

print("")

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])
