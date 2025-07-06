# Zavier Gaines
# June 30 2025
# P3HW1_GainesZavier
# all this does is gets ya grade average like those grade calcs you find online

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# now we putting all them in a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# this part finds lowest, highest, total and average
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display results with exact format
print()
print('------------Results-------------')
print('Lowest Grade:   ', format(low, '.1f'))
print('Highest Grade:  ', format(high, '.1f'))
print('Sum of Grades:  ', format(total, '.1f'))
print('Average:        ', format(avg, '.2f'))
print('--------------------------------')

# Determine letter grade for average
print()
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
