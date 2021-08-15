# logical Operators

# and
# or
# not

highIncome = True
goodCredit = True

if highIncome and goodCredit:
    print("Eligible")
else:
    print("Not eligible")

print("---------------------")

highIncome = False
goodCredit = True

if highIncome or goodCredit:
    print("Eligible")
else:
    print("Not eligible")

print("---------------------")

highIncome = False
goodCredit = True
student = True

if not student:
    print("Eligible")
else:
    print("Not eligible")

print("---------------------")

highIncome = False
goodCredit = True
student = False

if (highIncome or goodCredit) and not student:
    print("Eligible")
else:
    print("Not eligible")
