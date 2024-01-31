# Python have 3 logical oparator  "and", "or", and "not"

# high_income = False
# good_credit = True

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")


# high_income = False
# good_credit = True

# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# high_income = False
# good_credit = True
# student = True

# if not student:
#     print("Eligible")
# else:
#     print("Not Eligible")

high_income = False
good_credit = True
student = False

if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
