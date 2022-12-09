inputFile = open("input", "r")
grid = []
for line in inputFile:
    grid.append(list(map(int, line.strip())))
rotatedGrid = list(zip(*grid[::-1]))

count = 0
for y in range(len(grid)):
    if y == 0 or y == len(grid)-1:
        count += len(grid[y])
    else:
        for x in range(len(grid[y])):
            if x == 0 or x == len(grid[y])-1:
                count += 1
            else:
                inverseY = len(rotatedGrid[x]) - y - 1
                l = max(grid[y][:x])
                r = max(grid[y][x+1:])
                d = max(rotatedGrid[x][:inverseY])
                u = max(rotatedGrid[x][inverseY+1:])
                if min(l,r,d,u) < grid[y][x]:
                    count += 1
print(count)