file = open("Day 2 puzzle.txt", "r")

## PART 1
# score = 0

# def result(you, me):
#     points = 0
#     if you == "A":
#         if me == "X":
#             points += 1
#             points += 3
#         elif me == "Y":
#             points += 2
#             points += 6
#         elif me == "Z":
#             points += 3
#             points += 0
#     elif you == "B":
#         if me == "X":
#             points += 1
#             points += 0
#         elif me == "Y":
#             points += 2
#             points += 3
#         elif me == "Z":
#             points += 3
#             points += 6
#     elif you == "C":
#         if me == "X":
#             points += 1
#             points += 6
#         if me == "Y":
#             points += 2
#             points += 0
#         elif me == "Z":
#             points += 3
#             points += 3
            
#     return points
    

# for line in file:
#     line = line.replace("\n", "")
#     parts = line.split(" ")
#     youMove = parts[0]
#     meMove = parts[1]
    
#     score += result(youMove, meMove)
    
# print(score)
    
# PART 2

score = 0

def result(you, me):
    
    win = 0
    move = 0
    if you == 'A' and me == 'X':
        win += 0
        move += 3
    elif you == 'A' and me == 'Y':
        win += 3
        move += 1
    elif you == 'A' and me == 'Z':
        win += 6
        move += 2
    elif you == 'B' and me == 'X':
        win += 0
        move += 1
    elif you == 'B' and me == 'Y':
        win += 3
        move += 2
    elif you == 'B' and me == 'Z':
        win += 6
        move += 3
    elif you == 'C' and me == 'X':
        win += 0
        move += 2
    elif you == 'C' and me == 'Y':
        win += 3
        move += 3
    elif you == 'C' and me == 'Z':
        win += 6
        move += 1
    
    return win + move

for line in file:
    line = line.replace("\n", "")
    parts = line.split(" ")
    youMove = parts[0]
    meMove = parts[1]
    
    score += result(youMove, meMove)
    
print(score)