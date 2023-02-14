with open('Day 4 puzzle.txt') as f:
    lines = f.read().rstrip('\n').split('\n')

# PART 1
     
# count = 0
# row = 0
# for i in lines:
#     parts = i.split(",")
#     first = parts[0].split("-")
#     second = parts[1].split("-")

#     if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
#         count += 1
#     elif int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
#         count+=1
#     row +=1

# print(count)


# PART 2     

count = 0
row = 0
for i in lines:
    parts = i.split(",")
    first = parts[0].split("-")
    second = parts[1].split("-")


    for i in parts:
        
        if (int(second[1]) < int(first[0]) or int(second[0]) > int(first[1])):

            count += 1 

            break


print(len(lines) - count)
