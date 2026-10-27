print("-----Shopping cart ------")
cart=[]
while True:
    print("\n 1.add item")
    print("2.remove")
    print("3.view cart")
    print("4.sort cart")
    print("5.total items")
    print("6.exit")
    choice=input("please enter your choice:")
    if choice=="1":
        item=input("enter item:")
        cart.append(item)
        print(f"{item} added successfully")
    if choice=="2":
        item=input("please enter the item that need to be removed")
        if item in cart :
            cart.remove(item)
            print(f"{item} has removed")
        else:
            print("item not found")
    elif choice=="3":
        print("Your cart")
        if len(cart)==0:
            print("cart is empty")
        else:
            for item in cart:
                print(item)   
    elif choice=="4":
        cart.sort()
        print("cart is sorted")
        print(cart)
    elif choice=="5":
        print(f"total items:{len(cart)}")
    elif choice=="6":
        print("THANK YOU")
        break
    else:
        print("invalid number") 
