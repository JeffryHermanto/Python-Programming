# For Loops

for number in range(3):
    print("Attempt", number)

print('')

for number in range(3):
    print("Attempt", number + 1)

print('')

for number in range(3):
    print("Attempt", number + 1, (number + 1) * '.')

print('')

for number in range(1, 4):
    print("Attempt", number, number * '.')

print('')

# Add step in the last range argument
for number in range(1, 10, 2):
    print("Attempt", number, number * '.')
