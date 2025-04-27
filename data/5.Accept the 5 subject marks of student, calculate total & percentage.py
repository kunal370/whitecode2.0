"""
5.	Accept the 5 subject marks of student, calculate total & percentage
Per > 75 ‘ Grade A+’
Per > 60 and per<=75 ‘Grade A’
Per >=40 and per <=60 ‘Grade B’
Per < 40 → ‘Fail’
"""

phy=float(input("enter the physics marks"))
chem=float(input("enter the chem marks"))
maths=float(input("enter the maths marks"))
bio=float(input("enter the bio marks"))
eng=float(input("enter the eng marks"))

per=((phy+chem+maths+bio+eng)/500)*100
print(per)

if per>75:
    print("grade- A")
elif per>60 and per<=75:
    print("grade- B")
elif per>40 and per<=60:
    print("grade- C")
else:
    print("fail")
