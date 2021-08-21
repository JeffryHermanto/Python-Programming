# Sorting Lists

numbers = [3, 51, 2, 8, 6]

numbers.sort()
print(numbers)

print("")

numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(numbers)

print("")

numbers = [3, 51, 2, 8, 6]
print(sorted(numbers))
print(numbers)

print("")

numbers = [3, 51, 2, 8, 6]
print(sorted(numbers, reverse=True))
print(numbers)

print("")

items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
