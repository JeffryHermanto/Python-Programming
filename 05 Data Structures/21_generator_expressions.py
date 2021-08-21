# Generator Expressions

# In situations where we're dealing with a large data set, or potentially an infinite stream of data, use a generator expression to create a generator object.

from sys import getsizeof

values = (x * 2 for x in range(10))
print(values)

for x in values:
    print(x)

print("")

values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))

values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
