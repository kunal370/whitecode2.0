"""41	Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
"""

class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.stu_name=name
        self.sub1marks=sub1
        self.sub2marks = sub2
        self.sub3marks = sub3

    def avg_marks(self):
        avg=(self.sub1marks+self.sub2marks+self.sub3marks)/3
        print("average is: ",avg)

s1=Student("sonu",89,78,90)
s1.avg_marks()