# Tuples
# A read only list

point = 1, 2
print(point)

point = (1, 2) + (3, 4)
print(point)

point = (1, 2) * 3
print(point)

point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)

print("")

point = (1, 2, 3)
print(point[0])
print(point[0:2])
x, y, z = point
print("x", x)
print("y", y)
print("z", z)

if 10 in point:
    print("exists")
else:
    print("10 not exists")
