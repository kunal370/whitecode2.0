"""
function
31	WAF to print the elements of a list in a single line. ( list is the parameter)
"""

list1=[9,8,7,6,5,4,3,2,1,0]

def single_line(a):
    for i in a :
        print(i,end=" ")
    return a
single_line(list1)