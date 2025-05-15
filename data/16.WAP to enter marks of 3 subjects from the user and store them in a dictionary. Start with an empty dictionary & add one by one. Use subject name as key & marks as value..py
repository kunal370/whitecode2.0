"""
16	WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
"""

student={}
sub1=input("enter name of sub1: ")
marks=float(input("enter marks  of sub1: "))
student.update({sub1:marks})
sub2=input("enter name of sub2: ")
marks=float(input("enter marks  of sub2: "))
student.update({sub2:marks})
sub3=input("enter name of sub3: ")
marks=float(input("enter marks  of sub3: "))
student.update({sub3:marks})

print(student)