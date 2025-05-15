"""

28.	5. Write a Python program to find sum of all even numbers between 1 to n.
"""
n=20
i=0
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
        print(i)
    i+=1
print("sum is",sum)