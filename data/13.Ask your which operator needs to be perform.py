"""

13.	1. Ask your which operator needs to be perform + - * /


"""

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
selct=int(input("select the operator"))

match selct:
    case 1:
        print("selected addition")
        a=int(input("enter the numbers"))
        b=int(input("enter the numbers"))
        sum=a+b
        print("addition is : ",sum)

    case 2:
        print("selected subtraction")
        a = int(input("enter the numbers"))
        b = int(input("enter the numbers"))
        sub = a - b
        print("subtraction is : ", sub)

    case 3:
        print("selected multiplication")
        a = int(input("enter the numbers"))
        b = int(input("enter the numbers"))
        mul = a * b
        print("multiplication is : ", mul)

    case 4:
        print("selected division")
        a = int(input("enter the numbers"))
        b = int(input("enter the numbers"))
        div = a /b
        print("division is : ", div)

    case default:
        print("invalid")




