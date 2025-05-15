"""
20.	Accept a number & check number is prime number or not
"""

num=int(input("enter the number: "))
check=0

if num==1 or num==0:
    print("not prime")

for i in range(2,num):
    if num%i==0:
        check=1

if check==1:
    print("not prime")
else:
    print("prime")