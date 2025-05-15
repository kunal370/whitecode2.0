"""
35	Write a recursive function to print all elements in a list.
Hint : use list & index as parameters.
"""


fruits=["apple","banana","mango","pineapple","grapes"]

def print_all(list1,idx=0):
    if idx==len(list1):
        return
    print(list1[idx])
    print_all(list1,idx+1)
print(print_all(fruits))


