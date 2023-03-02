with open("Day 7 puzzle.txt") as f:
    lines = f.read().rstrip('\n').split('\n')

#print(lines)

path = "/home"
my_dictionary = {"/home": 0}

for command in lines:
    # commands starting with $
    if command[0] == "$":

        # ignore if ls or files
        if command[2:4] == "ls":
            continue
        # manage changing paths
        elif command[2:4] == "cd":

            # go back to root
            if command[5:6] == "/":
                path = "/home"
            
            # go back in path
            elif command[5:7] == "..":
                path = path[:path.rfind("/")] # rfind gives us the index of the last occuring character we define

            # change path
            else:
                dir_name = command[5:] # getting name of new directory
                path = path + "/" + dir_name # adding new directory to path
                my_dictionary.update({path:0})

    # do nothing when listing directories available
    elif command[0:3] == "dir":
        continue


    # get the file size and change directories in which it was found
    else:
        size = int(command[:command.find(" ")]) # get the size of the file, find gets first instance

        dir = path
        for i in range(path.count("/")):
            my_dictionary[dir] += size
            dir = dir[:dir.rfind("/")]

# for dir in my_directory:
#     print(dir, my_directory[dir])
total = 0

# space required (total) minus space unused
limit = 30000000 - (70000000 - my_dictionary["/home"])
#print(limit)
valid_dirs = []



for dir in my_dictionary:
    
    # PART 1
    if my_dictionary[dir] <= 100000:
        total += my_dictionary[dir]

    # PART 2
    if limit <= my_dictionary[dir]:
        valid_dirs.append(my_dictionary[dir])
    smallest = min(valid_dirs)

print("Part 1 answer:", total)
print("Part 2 answer:", smallest)