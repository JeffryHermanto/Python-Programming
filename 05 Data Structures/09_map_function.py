# Map Function

items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12),
]

# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)

prices = list(map(lambda item: item[1], items))
print(prices)
