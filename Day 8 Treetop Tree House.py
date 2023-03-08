with open("Day 8 puzzle.txt") as f:
    matrix = f.read().rstrip('\n').split('\n')
    
ROWS = len(matrix)
COLUMNS = len(matrix[0])

edge_trees = (2 * ROWS) + ((COLUMNS-2) * 2)
visible_trees = edge_trees

print(edge_trees)

for row in range(1, ROWS-1):
    for col in range(1, COLUMNS-1):
        tree = matrix[row][col]
        
        left = []
        for i in range(1, col+1):
            left.append(matrix[row][col-i])
        
        right = []
        for i in range(1, COLUMNS - col):
            right.append(matrix[row][col+i])
        
        # up = [matrix[row-i][col] for i in range(1, row+1)]
        # down = [matrix[row+i][col-i] for i in range(1, ROWS - row)]
        up = []
        for i in range (1, row + 1):
            up.append(matrix[row-i][col])
            
        down = []
        for i in range(1,ROWS - row):
            down.append(matrix[row+i][col])
            
        # PART 1
        if max(left)<tree or max(right)<tree or max(up)<tree or max(down)<tree:
            visible_trees += 1

print("Answer to part 1:", visible_trees)