# Adding or Removing Items

letters = ["a", "b", "c"]

# Add
letters.append("d")
print(letters)

letters.insert(0, "-")
print(letters)

# Remove
letters.pop()
print(letters)

letters.pop(0)
print(letters)

letters.remove("b")
print(letters)

del letters[0:1]
print(letters)

letters.clear()
print(letters)
