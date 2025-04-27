"""
45	create a class called order which stores item and its price
use dunder function __get__() to convey that: order1>order2 if price of order1>price of order2
"""

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, otherproduct):
        return  self.price>otherproduct.price

ord1=Order("phone",28000)
ord2=Order("laptop",74999)
print(ord2>ord1)
