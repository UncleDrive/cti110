# The first thing my program does is ask you for the budget for the trip
# Then after that it ask you where your vacation trip will be at
# After that its gonna ask how much you spend on gas
# then adfter that its gonna ask you what the hotel and accomidtion
# Afte this it will ask  how much you need for food eats
# finally you is done and it will tell you the prices of your stuff and give you your final balance
# now u got ur budget congrats bud enjoy vacation 


# Zavier Gaines
# June 16 2025
# P1HW2a
# the thign we are doing is getting the budget for our vactation and expenses

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
print()

place = input("Enter your travel destination: ")
print()

gas = int(input("How much do you think you will spend on gas? "))
print()

hotel = int(input("Approximately how much will you need for accomidation/hotel? "))
print()

food = int(input("Last how much do you need for food? "))
print()

total = gas + hotel + food
finalmoney = budget - total

print("------------Travel Expenses------------")
print ("Location:", place)
print("Initial Budget:", budget)
print( )
print("Fuel:", gas)
print ("Accomidation:", hotel)
print("Food:", food)
print()
print("Remaining Balance:", finalmoney)
