"""

12.	When you are writing any code for menu driven application
Example 1: 1. Eng
           2. Hindi
           3. Marathi
               1 1. Prepaid
                 2. Postpaid
                         1 1. Bal
                           2. Plans * to talk to customer care exec

"""
from collections import defaultdict

print("1.english")
print("2.hindi")
print("3.marathi")
lang=int(input("select language: "))

match lang:
    case 1:
        print("you have selected eng")
        print("1.prepaid")
        print("2.postpaid")
        plan=int(input("select plan"))
        match plan:
            case 1:
                print("selected prepaid plan")
                print("1.balance")
                print("2.Plans")
                support = int(input("select plan"))
                match support:
                    case 1:
                        print("your balance is 00$")
                    case 2:
                        print("you dont have active plan")
                    case default:
                        print("invalid")

            case 2:
                print("selected postpaid plan")
                print("1.balance")
                print("2.Plans")
                support = int(input("select plan"))
                match support:
                    case 1:
                        print("your balance is 00$")
                    case 2:
                        print("you dont have active plan")
                    case default:
                        print("invalid")
            case default:
                print("invalid")

    case 2:
        print("you have selected hindi")
        print("1.prepaid")
        print("2.postpaid")
        plan = int(input("select plan"))
        match plan:
            case 1:
                print("selected prepaid plan")
                print("1.balance")
                print("2.Plans")
                support = int(input("select plan"))
                match support:
                    case 1:
                        print("your balance is 00$")
                    case 2:
                        print("you dont have active plan")
                    case default:
                        print("invalid")

            case 2:
                print("selected postpaid plan")
                print("1.balance")
                print("2.Plans")
                support = int(input("select plan"))
                match support:
                    case 1:
                        print("your balance is 00$")
                    case 2:
                        print("you dont have active plan")
                    case default:
                        print("invalid")
            case default:
                print("invalid")

    case 3:
        print("you have selected marathi")
        print("1.prepaid")
        print("2.postpaid")
        plan = int(input("select plan"))
        match plan:
            case 1:
                print("selected prepaid plan")
                print("1.balance")
                print("2.Plans")
                support = int(input("select plan"))
                match support:
                    case 1:
                        print("your balance is 00$")
                    case 2:
                        print("you dont have active plan")
                    case default:
                        print("invalid")

            case 2:
                print("selected postpaid plan")
                print("1.balance")
                print("2.Plans")
                support = int(input("select plan"))
                match support:
                    case 1:
                        print("your balance is 00$")
                    case 2:
                        print("you dont have active plan")
                    case default:
                        print("invalid")
            case default:
                print("invalid")
    case default:
        print("invalid")