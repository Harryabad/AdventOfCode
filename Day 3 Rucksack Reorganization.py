file = open("Day 3 puzzle.txt", "r")

# Not needed
# priority = {
#     "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g":7, "h": 8, "i": 9, "j": 10,
#     "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
#     "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
#     "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36,
#     "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46,
#     "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52
# }

# Part 1
# sum = 0

# for line in file:
#     line = line.replace("\n", "")
    
#     i = len(line)
#     print("String Length: ", i)
    
#     if i%2 == 0:
#         str1 = line[0:i//2]
#         str2 = line[i//2:]
#         print("String First Half: ", str1)
#         print("String Second Half: ", str2)
#         for x in set(str1):
#             for y in set(str2):
#                 if x == y:
#                     if ord(x) >= 97 and ord(x) <= 122:
#                         sum += (ord(x) - 96)
#                     else:
#                         sum += (ord(x) - 38)
        
#     else:
#         st1 = line[0:i//2+1]
#         str2 = line[(i//2+1):]
#         print("String First Half: ", str1)
#         print("String Second Half: ", str2)
#         for x in str1:
#             for y in str2:
#                 if x == y:
#                     if ord(x) >= 97 and ord(x) <= 122:
#                         sum += (ord(x) - 96)     
#                     else:
#                         sum += (ord(x) - 38)
    
# print(sum)

# Part 2
lines = []
sum = 0
y = 0
usedletters = " "
for line in file:
    
    line = line.replace("\n", "")
    lines.append(line)
    
    if len(lines) >= 3:
        #print(lines)
        for x in lines[0]:
            if x in lines[1] and x in lines[2]:


                usedletters += x
                break                                  
        lines = []
        
usedletters = usedletters.replace(' ', '')


for x in usedletters:
    
    if x.isupper():
        sum = sum + (ord(x)-38)
    elif x.islower():
        sum = sum + (ord(x)-96)

print(sum)
print("Hello")
    

                
