"""
28	WAP to find the sum of first n numbers. (using while)
"""
n=int(input("enter the number"))
i=0
sum=0
while i<=n:
    print(i)
    sum+=i
    i+=1
print("print total sum",sum)