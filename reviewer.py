age = int(input("Enter your age ----->  "))
revenue = float(input("What is your monthly revenue? ------>  "))
credit_score = int(input("Enter your Credit score ----->  "))
years_in_business = float(input("Years in business ----->  "))
has_default = bool(input("File For Bankruptcy ----->  "))
collateral = str(input("Enter CN ----->  "))
c_value = float(input("Collateral Value -----> "))

max_loan = 0
base_fee = 0

if age >= 21 and years_in_business >= 2.0 and has_default == False:
    print("BASELINE PASSED")
    if credit_score >= 720: #teir 1
        max_loan = revenue * 3
        print("MAXIMUM LOANABLE AMOUNT IS SET TO",max_loan)
        print("HIGH CREDIT SCORE")
        if revenue >= 50000:
            print("REVENUE HIGHER THAN 50K ")
            base_fee = max_loan * 0.015
            print("Base fee rate is set to", base_fee)
        else:
            print("revenue lower than 50k")
            base_fee = max_loan * 0.025
            print("base fee rate is set to", base_fee)

            if c_value >= max_loan:
                print("collateral ", collateral, "with a value of ",c_value, "is ACCEPTED")
            else:
                print("Rejected: insufficient collateral value for ", collateral)

                if c_value % 5000 != 0:
                    print("Additional charge added")
                    base_fee += 250
                    print("Updated base fee is ",base_fee)

    elif credit_score >= 620 and credit_score < 720:
        print("credit score within range of 620 to 720")
        max_loan = revenue * 1.5
        print("maximum loan for this credit score is ",max_loan)
        if years_in_business >= 5:
            print("business is more than 5 years")
            base_fee = max_loan * 0.02
            print("Base fee rate is set to ", base_fee)
        else:
            print("business year less than 5 years")
            base_fee = max_loan * 0.035
            print("base fee rate is set to ", base_fee)

    elif credit_score < 620 and credit_score >= 1:
        print("Credit score is low")
    else:
        print("INVALID")
else:
    print("BASELINE FAILED")
