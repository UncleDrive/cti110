# Zavier Gaines
# June 30 2025
# P2HW2
# getting the grades of eacg of the module

# Pseudocode:
# post your grades each timne
# keep your grade for each listed
# this would be the lowest grade you got
# this would be the highest grade you got
# all grade totals
# your average

grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

grades = [grade1, grade2, grade3, grade4, grade5, grade6]

print("\n------------Results------------")
print("Lowest Grade:      ", min(grades))
print("Highest Grade:     ", max(grades))
print("Sum of Grades:     ", sum(grades))
print("Average:           ", format(sum(grades)/6, ".2f"))

print("----------------------------------------")
