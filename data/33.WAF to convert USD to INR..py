"""
33	WAF to convert USD to INR.
"""

#1usd=85.82

usd=float(input("enter doller $: "))
def inr_convert(a):
    inr=85.82*a
    print("INR is ",inr)

inr_convert(usd)
