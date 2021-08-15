# Exercise

# Display even number from 1 to 10
# 2
# 4
# 6
# 8
# We have 4 even numbers

count = 0

for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)

print(f"We have {count} even numbers")
