# Sets
# Unordered collection without duplicates

numbers = [1, 1, 2, 3, 4]

first = set(numbers)
print(first)

second = {1, 5}

# Union
print(first | second)

# Intersection
print(first & second)

# Difference
print(first - second)

# Items that are either in the first or second set but not both
print(first ^ second)

if 1 in first:
    print("yes")
