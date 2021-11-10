has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
elif has_high_income or has_good_credit:
    print("Only one condition")


has_criminal_record = False
if not has_criminal_record and has_good_credit:
    print("Eligible for loan")

if not has_criminal_record and not has_good_credit:
    print("Not eligible for loan")