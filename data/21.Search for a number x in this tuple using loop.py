"""
21	Search for a number x in this tuple using loop
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
"""
x=int(input("search no: "))
list1=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

i=0
while i<len(list1):
    if x==list1[i]:
        print(i,"found at: ",i)
    else:
        print(i,"not found")
    i+=1
print("list ended")