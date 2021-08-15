# For..Else

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

print('')

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

print('')

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
