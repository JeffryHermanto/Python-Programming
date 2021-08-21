# Dictionaries

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point)
print(point["x"])

point["x"] = 10
print(point)

point["z"] = 20
print(point)

print(point.get("a"))
print(point.get("a", 0))

del point["x"]
print(point)

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)
