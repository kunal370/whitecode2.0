"""

9.	Accept the bike price from user & add road tax as follows
Price > 80000 15 % TAX
Price > 40000 & <80000 10% TAX
Else 5% TAX

"""

price=float(input("enter the price of your bike: "))
if price>80000:
    tax=price*15/100
    print("tax is 15 %: ",tax)
    cost=tax+price
    print("total cost: ",cost)

elif price>40000 and price<80000:
    tax=price*10/100
    print("tax is 10 %: ",tax)
    cost=tax+price
    print("total cost: ",cost)
else:
    tax=price*5/100
    cost=tax+price
    print("tax is 5 %: ",tax)
    print("total cost: ",cost)