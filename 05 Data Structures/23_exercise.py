# Exercise

from pprint import pprint

# Find the most repeated character in this text
sentence = "This is a common interview question"

charFrequency = {}

for char in sentence:
    if char in charFrequency:
        charFrequency[char] += 1
    else:
        charFrequency[char] = 1

pprint(charFrequency)
print("")

sortedCharFrequency = sorted(
    charFrequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(sortedCharFrequency)
print("")
print("The most repeated character:", sortedCharFrequency[0])
