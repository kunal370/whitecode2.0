"""
30.	7. Write a Python program to count number of digits in any number
"""

# n=5678
# n=len(str(n))
# print(n)

n=-12345
i=1
n=abs(n)
while i<=n:
    n=n//10
    i+=1
print(i)

