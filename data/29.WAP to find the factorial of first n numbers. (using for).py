"""
29	WAP to find the factorial of first n numbers. (using for)
"""
n=int(input("no. : "))
fact=1
for i in range(1,n+1):
    print(i)
    fact*=i
print("factorial is ",fact)