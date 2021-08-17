# Short-circuit Evaluation

highIncome = True
goodCredit = True
student = False

# As soon as one of these arguments is false, the evaluation stops
if highIncome and goodCredit and not student:
    print("Eligible")
