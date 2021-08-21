# Looping over Lists

letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

print("")

for letter in enumerate(letters):
    print(letter)

print("")

for letter in enumerate(letters):
    print(letter[0], letter[1])

print("")

for index, letter in enumerate(letters):
    print(index, letter)
