# Zavier Gaines
# July 7 2025
# P4HW1_GainesZavier
# getting scores and taking avaerages and grades

# pseudocode:
# how many scores you need to enter
# loop that many times and get a valid score 0 to 100
# keep askin if the score not valid
# store scores in a list
# drop the lowest score
# show lowest score
# show the list after dropping the lowest
# show average
# show letter grade based on average

scores = []

num_scores = int(input("how many scores do you want to enter"))

for i in range(num_scores):
    print()
    score = float(input("Enter score #" + str(i + 1) + ": "))
    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(i + 1) + " again: "))
    scores.append(score)

print()
print("--------------Results--------------")
lowest = min(scores)
print("Lowest Score  :", lowest)

scores.remove(lowest)
print("Modified List :", scores)

average = sum(scores) / len(scores)
print("Scores Average:", round(average, 2))

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade         :", grade)
print("-----------------------------------")
