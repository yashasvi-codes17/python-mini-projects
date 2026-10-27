#smart bill calculator
product1=input("enter the first product details")
price1=float(input("enter the price 1 details"))
product2=input("enter the second product details")
price2=float(input("enter the price 2 details"))
product3=input("enter the third product details")
price3=float(input("enter the price 3 details"))
total=price1+price2+price3
gst=18
gst_amount=total*gst/100
final_amount=total+gst_amount
print("\n the bill calculator")
print(f"product1 is {product1}")
print(f"price1 is {price1}")
print(f"product2 is {product2}")
print(f"price1 is {price2p}")
print(f"product3 is {product3}")
print(f"price1 is {price3}")
print("---------------------")
print(f"total is:{total}")
print(f"gst amount is{gst_amount}")
print(f"the amount after adding gst {final_amount}")
print("thank you")