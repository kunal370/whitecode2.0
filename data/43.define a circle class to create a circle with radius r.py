"""
43	define a circle class to create a circle with radius r
using the constructor define area() method of class
which calculates the area of the circle
define parameter() method of the class
which allows you to calculate perimeter of the circle


area=3.14*r*r
per=2*3.14*r
"""

class Circle:
    def __init__(self,radius):
        self.r=radius

    def area(self):
        area=3.14*self.r**2
        return area

    def per(self):
        per=2*3.14*self.r
        return per
    def all(self):
        print("area is: ",self.area())
        print("perimeter is: ",self.per())


c1=Circle(3)
c1.all()