print("ALL LETTERS MUST BE IN CAPITALS.")
surname = input("What is your surname?" )
print(surname.capitalize())
other_names=input("What is/are your other names? ")
age=int(input("What is your age? "))
if age<18:
    print("Sorry, you are ineligible to create an account")
else:
    email=input("What is your email address? ")
    contact=input("What is your mobile number? ")
if len(contact)!=10:
    print("Invalid mobile nuymber? ")
else:
    country=input("What country are you from? ")
    print("Congratulations on creating your new account")
    print("Your account number is GH-1234-5678")
    real_acc_num= "GH-1234-5678"
    acc_num=input("Please input your account number as you see: ")  
if acc_num!=real_acc_num:
    print("Sorry, that is incorrect, check and try again.")
else:
    pin=input("Type a seven digit pin to secure your a account")
if len(pin)!=7:
    print("pin should be seven digit please")
else:
    ans=int(input("Would you like to make your first deposit YES(1)/NO(0)? "))
if ans==1:
    dep=input("How much would you like to deposit in cedis? ")
    print("You have succesffully depositted "+dep+"cedis into your new account,")
else:
    print(" Thank you for patronising us")
    