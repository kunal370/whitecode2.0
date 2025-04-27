"""

40	From a file containing numbers separated by comma, print the count of even numbers.
"""
count=0
with open("nums.txt","r")as f:
    data=f.read()
    print(data)
    nums=data.split(",")
    for i in nums:
        if int(i)%2==0:
            count+=1
print(count)