"""
22.	4. Accept the number & check number is Armstrong number or not
"""

num=int(input("enter the number: "))
length=len(str(num))
sum=0
temp=num
while temp>0:
    res=temp%10
    sum=sum+res**length
    temp=temp//10

if num==sum:
    print("armstrong")
else:
    print("not armstrong")
