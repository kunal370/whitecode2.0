"""
function
32	WAF to find the factorial of n. (n is the parameter)
"""

n=5

def factorial_no(a):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i+=1
    print("factorial is: ",fact)
factorial_no(n)