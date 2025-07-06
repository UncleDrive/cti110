# Zavier Gaines
# June 30th 2025
# P3LAB_GainesZavier
# for this assigment we are workling with currences and decimals points

 
amount = float(input("Enter the amount of money as a float: $"))

# Convert amount to cents (whole number)
cents = int(round(amount * 100))

# Start with dollars
dollars = cents // 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25


dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

# Display results
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")
    
else:
    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(str(dollars) + " Dollars")

    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(str(quarters) + " Quarters")

    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(str(dimes) + " Dimes")

    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(str(nickels) + " Nickels")

    if pennies == 1:
        print("1 Penny")
    elif pennies > 1:
        print(str(pennies) + " Pennies")
