# Zavier Gaines
# July 14 2025
# P5LAB_GainesZavier
# copying a self checkout lke method

import random

def disperse_change(change):
    cents = int(round(change * 100))

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(str(dollars) + " Dollars")
    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(str(quarters) + " Quarters")
    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(str(dimes) + " Dimes")
    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(str(nickels) + " Nickels")
    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(str(pennies) + " Pennies")

def main():
    total = round(random.uniform(0.01, 100.00), 2)
    print("You owe $" + str(total))

    paid = float(input("How much cash will you put in the self-checkout? "))

    if paid < total:
        print("Not enough money.")
    elif paid == total:
        print("Exact change. No change is due.")
    else:
        change = round(paid - total, 2)
        print("Change is: $" + str(change))
        disperse_change(change)

main()
