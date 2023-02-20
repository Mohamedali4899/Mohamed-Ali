import time 
#Processing time for ATM card
time.sleep(5)
print("Welcome to ABCD bank ATM")
#Taking PIN number from user
password = 1234
pin = int(input("Enter your password:"))
# Account Balance of user
Balance = 60000
if pin == password:
# Showing option to user
    print("""
            1 == Check balance
            2 == Deposit amount
            3 == Withdraw amount
            4 == Exit """)
    
# Taking option from user
    try:
        option = int(input("Select your option..."))
    except:
        print("Enter your option correctly")

    if option == 1:
         print(f"Your account balance is {Balance}")

    elif option == 2:
        Deposit_amount = int(input("Enter your Deposit amount:"))
        balance = Balance + Deposit_amount
        print(f"{Deposit_amount} is credited to your account")
        print(f"Your account balance is {Balance}")
  

    elif option == 3:
        Withdraw_amount = int(input("Enter your Withdraw amount:"))
        Balance = Balance - Withdraw_amount
        print(f"{Withdraw_amount} is debited from your account")
        print(f"Your account balance is {Balance}")

    elif option == 4:
        print("Have a nice day...")
        

    
    

