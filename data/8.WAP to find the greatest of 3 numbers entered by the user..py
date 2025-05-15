"""
8	WAP to find the greatest of 3 numbers entered by the user.
"""

a=int(input("1st no: "))
b=int(input("3rd no: "))
c=int(input("2nd no: "))

if a>b and a>c:
    print(a,"is bigger")
elif b>a and b>c:
    print(b,"is bigger")
else:
    print(c,"is bigger")