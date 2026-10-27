print("-----simple calculator-----")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Invalid b value"
    return a/b
def power(a,b=2):
    return a**b
def total_number(numbers):
    total=0
    for number in numbers:
        total=total+number
    return total
while(True):
    print("\n 1,add")
    print("2,subtract")
    print("3.multiplication")
    print("4.division")
    print("5.power")
    print("6.exit")
    ch=input("enter your choice")
    if ch=="6":
        print("calculator closed")
        break
    if ch=="5":
        number=float(input("enter a number:"))
        result=power(number)
        print(result)
    if ch not in ("1","2","3","4"):
        print("Invalid choice")
        continue
    num1=float(input("enter a number 1:"))
    num2=float(input("enter a number 2:"))
    if ch=="1":
        result=add(num1,num2)
    elif ch=="2":
        result=sub(num1,num2)
    elif ch=="3":
        result=mul(num1,num2)
    elif ch=="4":
        result=div(num1,num2)
    print(f"Result: {result}")
