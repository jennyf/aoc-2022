def getScenicScore(x, y):
    global grid
    l = r = u = d = 0
    h = grid[y][x]
    for i in range(x-1, -1, -1):
        if grid[y][i] < h:
            l += 1
        else:
            l += 1
            break
    for i in range(x+1, len(grid)):
        if grid[y][i] < h:
            r += 1
        else:
            r += 1
            break
    for i in range(y-1, -1, -1):
        if grid[i][x] < h:
            u += 1
        else:
            u += 1
            break
    for i in range(y+1, len(grid)):
        if grid[i][x] < h:
            d += 1
        else:
            d += 1
            break    
    return l*r*u*d

inputFile = open("input", "r")
grid = []
for line in inputFile:
    grid.append(list(map(int, line.strip())))

bestScenicScore = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if y == 0 or y == len(grid)-1 or x == 0 or x == len(grid[y])-1:
            next
        else:
            score = getScenicScore(x, y)
            if score > bestScenicScore:
                bestScenicScore = score
print(bestScenicScore)