def moveTail():
    global hx, hy, tx, ty, visited
    dx = 1 if hx > tx else -1
    dy = 1 if hy > ty else -1
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return
    elif hx == tx:
        ty += dy
    elif hy == ty:
        tx += dx
    else:
        tx += dx
        ty += dy
    visited.add((tx, ty))

def move(direction, numMoves):
    global hx, hy, tx, ty
    for i in range(numMoves):
        match direction:
            case 'L':
                hx -= 1
                moveTail()
            case 'R':
                hx += 1
                moveTail()
            case 'U':
                hy += 1
                moveTail()
            case 'D':
                hy -= 1
                moveTail()

inputFile = open("input", "r")
hx = hy = tx = ty = 0
visited = {(0,0)}
for line in inputFile:
    direction = line.strip().split(' ')[0]
    numMoves = int(line.strip().split(' ')[1])
    move(direction, numMoves)

print(len(visited))