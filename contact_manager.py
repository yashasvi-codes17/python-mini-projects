print("context manager")
contacts={}
while True:
    print("\n1.add contact")
    print("2.view contact")
    print("3.search contact")
    print("4.delect contact")
    print("5.view unique contact")
    print("6.exit")
    choice=input("please select one")
    if choice=="1":
        name=input("enter name")
        phone=input("enter phone number")
        contacts[name]=phone
        print("contact add successfully")
    if choice=="2":
        if len(contacts)==0:
            print("no contacts found")
        else:
            print("the details are")
            for name,phone in contacts.items():
                print(f"{name}:{phone}")
    if choice=="3":
        name=input("enter name to search")
        phone=contacts.get(name)
        if phone:
            print(f"{name} number is {phone}")
        else:
            print("not found")
    elif choice=="4":
        name=input("enter name to delect:")
        if name in contacts:
            del contacts[name]
            print("contact is delected")
        else:
            print("not found")
    elif choice=="5":
        unique_name=set(contacts.keys())
        print("unique contacts:")
        print(unique_name)
    elif choice=="6":
        print("contact manager closed")
        break
    else:
        print("invalid choice")
        
