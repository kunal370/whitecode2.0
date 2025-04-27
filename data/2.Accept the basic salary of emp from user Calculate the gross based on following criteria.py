"""
2.	Accept the basic salary of emp from user Calculate the gross based on following criteria
Cal HRA 40% of basic
Cal DA 20% of basic
Cal PF 12 % of basic
Use PT =200
Calculate the gross salary of emp &
display the output gross= (bs+hra+da) -(pf+pt)
Bs = Hra - Da - Pf - Pt -200 Gross –

"""
PT=200
basic=float(input("enter basic salary: "))
HRA=(40/100)*basic
DA=(20/100)*basic
PF=(12/100)*basic
print(HRA)
print(DA)
print(PF)
gross=(basic+HRA+DA)-(PF+PT)
print("gross salary",gross)
