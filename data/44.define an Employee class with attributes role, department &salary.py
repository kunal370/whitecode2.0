"""

44	define an Employee class with attributes role, department &salary.
this class also has showdetails() method
create an engineer class that inherits  properties from employee
and has additional attributes : name and age
"""

class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.dept=department
        self.sal=salary

    def showdetails(self):
        print(self.role)
        print(self.dept)
        print(self.sal)


class Engineer(Employee):
    def __init__(self, name, age,role, department,salary):
        self.name=name
        self.age=age
        super().__init__(role,department,salary)

    def showdetails(self):
        print(self.name)
        print(self.age)
        super().showdetails()

e1=Engineer("sonu",23,"Software Engineer","IT","39000")
e1.showdetails()
