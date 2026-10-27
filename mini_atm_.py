#mini project 
print("----mini atm----")
correct_pin=1234
balance=5000
pin = int(input("Enter pin"))
if pin==correct_pin:
    print("login sucessful")
    print("1.check balance")
    print("2.withdraw money")
    print("3.deposite money")
    choice=int(input("please select one : "))
    if choice==1:
        print(f"the balance is {balance}")
    elif choice==2:
        amount=int(input("please enter the amount that your going to withdraw:"))
        if amount>0 and amount<=balance:
            balance=balance-amount
            print(f"the final balance is {balance}")
    elif choice==3:
        amount=int(input("please enter the amount that your going to deposite:"))
        if amount>0:
            balance=balance+amount
            print(f"the final amount is {balance}")
    else:
        print("please enter corrct choice")
else:
    print("your pin is wrong")                 

