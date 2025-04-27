"""
24	Search for a number x in this tuple using loop
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

"""
x=int(input("search no: "))
nums=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx=0
for i in nums:
    if x == i:
        print("found at idx=",idx)
    else:
        print("not found at",idx)
    idx=idx+1
