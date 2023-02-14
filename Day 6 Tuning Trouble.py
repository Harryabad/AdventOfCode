with open("Day 6 puzzle.txt") as f:
    lines = f.read().rstrip('\n').split('\n')

listy = []
newlist = []
count = 0
for i in lines:
    line = i
    
for i in line:
    listy.append(i)

for i in listy:
    count +=1
    newlist.append(i)
    if len(newlist) > 4:
        newlist = newlist[1:4]
        newlist.append(i)

        if (len(set(newlist)) == len(newlist)) and count > 4:
            print(count)
            break

        
# print(newlist)
# print(x == i)