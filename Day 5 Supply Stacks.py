with open("Day 5 puzzle.txt") as f:
    lines = f.read().rstrip('\n').split('\n')



# supermatrix = []
       
# for x in range(1,10):
#     listy = []
#     supermatrix.append(listy)
    
# for i in lines:
#     if i == "":
#         break
    
#     if (i[1] != ' '):
#         supermatrix[0].append(i[1])       
#     if (i[5] != ' '):
#         supermatrix[1].append(i[5])
#     if (i[9] != ' '):
#         supermatrix[2].append(i[9])    
#     if (i[13] != ' '):
#         supermatrix[3].append(i[13])
#     if (i[17] != ' '):
#         supermatrix[4].append(i[17])       
#     if (i[21] != ' '):
#         supermatrix[5].append(i[21])
#     if (i[25] != ' '):
#         supermatrix[6].append(i[25])    
#     if (i[29] != ' '):
#         supermatrix[7].append(i[29])
#     if (i[33] != ' '):
#         supermatrix[8].append(i[33])         
         

# for i in range(len(supermatrix)):
#     supermatrix[i] = supermatrix[i][::-1]


# for i in supermatrix:
#     print(i)
    
# print()


# with open('crates.txt') as f:
#     lines = f.read().rstrip('\n').split('\n\n')
    
# parts = lines[1].split('\n')

# #print(parts)

# for i in parts:
#     steps = i.split(' ')
#     numOfBoxes = int(steps[1])
#     fromLane = int(steps[3])-1
#     toLane = int(steps[5])-1
    
#     # get the required boxes from the lane
#     temp = (supermatrix[fromLane])[-numOfBoxes:]
#     # as we're collecting them all at once, the list must be reversed before placing them
#     temp = temp[::-1]
    
    
#     #print("move: " + str(numOfBoxes) + " from " + str(supermatrix[fromLane]) + " to " + str(supermatrix[toLane]))
    
#     # add temp boxes to new lane
#     supermatrix[toLane] += temp
#     # remove the temp boxes from the old lane
#     supermatrix[fromLane] = (supermatrix[fromLane])[:-numOfBoxes]
    
    
#     #print("boxes being moved: " + str(temp) + "  ||   newLaneUpdated" + str(supermatrix[toLane]))
#     #print("old lane " + str(supermatrix[fromLane]))
#     #print()

# for i in supermatrix:
#     print(i)
    
# print()
# #answer
# for i in supermatrix:
#     print((i[-1]).lower(), end='')


# PART 2



supermatrix = []
       
for x in range(1,10):
    listy = []
    supermatrix.append(listy)
    
for i in lines:
    if i == "":
        break
    
    if (i[1] != ' '):
        supermatrix[0].append(i[1])       
    if (i[5] != ' '):
        supermatrix[1].append(i[5])
    if (i[9] != ' '):
        supermatrix[2].append(i[9])    
    if (i[13] != ' '):
        supermatrix[3].append(i[13])
    if (i[17] != ' '):
        supermatrix[4].append(i[17])       
    if (i[21] != ' '):
        supermatrix[5].append(i[21])
    if (i[25] != ' '):
        supermatrix[6].append(i[25])    
    if (i[29] != ' '):
        supermatrix[7].append(i[29])
    if (i[33] != ' '):
        supermatrix[8].append(i[33])         
         

for i in range(len(supermatrix)):
    supermatrix[i] = supermatrix[i][::-1]


for i in supermatrix:
    print(i)
    
print()


with open("Day 5 puzzle.txt") as f:
    lines = f.read().rstrip('\n').split('\n\n')
    
parts = lines[1].split('\n')

#print(parts)

for i in parts:
    steps = i.split(' ')
    numOfBoxes = int(steps[1])
    fromLane = int(steps[3])-1
    toLane = int(steps[5])-1
    
    # get the required boxes from the lane
    temp = (supermatrix[fromLane])[-numOfBoxes:]
    
    # Part 2 means we can move multiple boxes up and down, no need to reverse
    #temp = temp[::-1]
    
    
    #print("move: " + str(numOfBoxes) + " from " + str(supermatrix[fromLane]) + " to " + str(supermatrix[toLane]))
    
    # add temp boxes to new lane
    supermatrix[toLane] += temp
    # remove the temp boxes from the old lane
    supermatrix[fromLane] = (supermatrix[fromLane])[:-numOfBoxes]
    
    
    #print("boxes being moved: " + str(temp) + "  ||   newLaneUpdated" + str(supermatrix[toLane]))
    #print("old lane " + str(supermatrix[fromLane]))
    #print()

for i in supermatrix:
    print(i)
    
print()
#answer
for i in supermatrix:
    print((i[-1]).lower(), end='')