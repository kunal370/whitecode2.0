"""
Recursion
34	Write a recursive function to calculate the sum of first n natural numbers.

"""
n=int(input("enter the no. "))
def sum_n(a):
    if a==0:
        return 0
    else:
        return sum_n(a-1)+a
print(sum_n(n))