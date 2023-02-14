file = open("Day 1 puzzle.txt", "r")
#print(file.read())
##PART 1
# highestCalories = 0
# highestElf = 0
# elfNum = 1
# calories = 0

# for line in file:
#     if line != "\n":
#         calories += int(line)
#         if calories > highestCalories:
#             highestCalories = calories
#             highestElf = elfNum
#     else:
#         elfNum += 1
#         calories = 0
    
# PART 2        
calories = 0
elfNum = 0

elflist = []
callist = []
for line in file:
    if line != "\n":
        calories += int(line)
    else: 
        elflist.append(elfNum)
        callist.append(calories)
        elfNum += 1
        calories = 0
               
#sorted(zip(callist, elflist), reverse=True)[:3]

topThree = sorted(zip(callist, elflist), reverse=True)[:3]

print(topThree)

totalCaloriesTopThree = topThree[0][0] + topThree[1][0] + topThree[2][0]
print(totalCaloriesTopThree)

        
# print(f"highest cal {highestCalories} from elf number {highestElf}")
        