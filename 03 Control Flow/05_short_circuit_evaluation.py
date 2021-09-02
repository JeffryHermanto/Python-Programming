# Short-circuit Evaluation

high_income = True
good_credit = True
student = False

# As soon as one of these arguments is false, the evaluation stops
if high_income and good_credit and not student:
    print("Eligible")
