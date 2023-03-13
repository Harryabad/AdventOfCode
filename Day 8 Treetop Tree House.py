with open("Day 8 puzzle.txt") as f:
    matrix = f.read().rstrip('\n').split('\n')
    
ROWS = len(matrix)
COLUMNS = len(matrix[0])

edge_trees = (2 * ROWS) + ((COLUMNS-2) * 2)
visible_trees = edge_trees

scores = []  # track scenic scores

#print(edge_trees)

for row in range(1, ROWS-1): # start at 1 so we dont have to count edges, -1 to skip the last row
    for col in range(1, COLUMNS-1): # same here
        tree = matrix[row][col]
        
        # Find all the trees on the left side, right side, up and down from the specific tree we're on.

        #Horizontal

        left = []
        for i in range(1, col+1): # plus 1 as upto and including the col we're in
            left.append(matrix[row][col-i]) # keeps going 1 to the left for the columns in each iteration
        
        right = []
        for i in range(1, COLUMNS - col): # COLUMNS is the end column (to the right) - the col we are in for the tree 
            right.append(matrix[row][col+i]) # keeps going 1 to the right for columns in each iteration
        
        #Vertical
        up = []
        for i in range (1, row + 1): # similar to left but going up
            up.append(matrix[row-i][col]) # up one row (-1) for each iteration
            
        down = []
        for i in range(1, ROWS - row): # similar to right but going down. total ROWS - the row we're in
            down.append(matrix[row+i][col]) # down one row (+1) for each iteration
        
        # left  [matrix[row][col-i] for i in range(1, col+1)]
        # right = [matrix[row][col+i] for i in range(1, COLUMS - col)]
        # up = [matrix[row-i][col] for i in range(1, row+1)]
        # down = [matrix[row+i][col-i] for i in range(1, ROWS - row)]


        # PART 1
        # compare the highest value of our four list [left, right, up. down] to our current tree.  if our tree is
        # higher in any. add it to the visible trees category
        if max(left)<tree or max(right)<tree or max(up)<tree or max(down)<tree:
            visible_trees += 1


        # PART 2
        score = 1 # Initialize the score to 1
        for lst in (left, right, up, down): # Loop through each of the four lists of adjacent trees
            tracker = 0 # Initialize a variable to keep track of how many trees we've seen so far
            for i in range(len(lst)): # Loop through each tree in the current list
                if lst[i] < tree: # If the height of the current tree is less than the height of our current tree
                    tracker += 1 # Increment the tracker variable
                elif lst[i] == tree: # If the height of the current tree is the same as the height of our current tree
                    tracker += 1 # Increment the tracker variable
                    break # Break out of the loop (we don't need to keep checking this list)
                else: # If the height of the current tree is greater than the height of our current tree
                    break # Break out of the loop (we don't need to keep checking this list)
            score *= tracker # Multiply the score by the number of trees we've seen in the current list
        scores.append(score) # Add the score to the list of scores for each tree



print("Answer to part 1:", visible_trees)
# Answer to part 1: 1849

print("Answer to part 2:", max(scores))
# Answer to part 2: 201600