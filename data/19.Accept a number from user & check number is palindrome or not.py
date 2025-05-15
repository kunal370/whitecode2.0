"""
19.	Accept a number from user & check number is palindrome or not
"""

num=int(input("no: "))
str1=str(num)
copy=str1[::-1]
if copy==str1:
    print("palindrome")
else:
    print("not palindrome")


