print ("Hello world")

age = int(input("Enter your age: --->   "))
is_employed = bool(input("Are you employed? (yes/no): ---> "))
credit_score = int(input("Enter your current credit score: ---> "))
annual_income = float(input("How much is your annual income? ---> "))
has_collateral = bool(input("Do you have a collateral? (Yes/No: --->"))

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("Applicant pass baseline requirements")
    if credit_score >= 750:  #Tier1   
       base_rate = 5.0
       print("You have a high credit score")
       if annual_income >= 100000:
          base_rate = 4.5
          print("You have a high salary and a high credit score")
    elif credit_score >= 600 and credit_score <750:
        if has_collateral -- True:
            base_rate = 7.0
            print("You have a High salary and high credit score, your interest rate is",base_rate")
    elif annual_income <= 40000:
        print("Low salary with fair credit score")
        base_rate = 9.5
        print("You have a high salary and high credit score your interest rate is, base rate")
    else:
        print("fair credit score with no collateral")
        base_rate =8.0
        print("You have a high salary and high credit score")    
                  
    else:
        print("failed")

else:
    print("Rejected ka boi")


    

          
    



