def moveTails():
    global knotCoords, visited
    for i in range(1, 10):
        hx = knotCoords[i-1][0]
        hy = knotCoords[i-1][1]
        tx = knotCoords[i][0]
        ty = knotCoords[i][1]
        dx = 1 if hx > tx else -1
        dy = 1 if hy > ty else -1
        if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
            return
        elif hx == tx:
            knotCoords[i] = (tx, ty+dy)
        elif hy == ty:
            knotCoords[i] = (tx+dx, ty)
        else:
            knotCoords[i] = (tx+dx, ty+dy)
    visited.add((knotCoords[9]))

def move(direction, numMoves):
    global knotCoords
    for i in range(numMoves):
        hx = knotCoords[0][0]
        hy = knotCoords[0][1]
        match direction:
            case 'L':
                knotCoords[0] = (hx-1, hy)
                moveTails()
            case 'R':
                knotCoords[0] = (hx+1, hy)
                moveTails()
            case 'U':
                knotCoords[0] = (hx, hy+1)
                moveTails()
            case 'D':
                knotCoords[0] = (hx, hy-1)
                moveTails()

inputFile = open("inputMedium", "r")
knotCoords = []
for i in range(10):
    knotCoords.append((0,0))
visited = {(0,0)}
for line in inputFile:
    direction = line.strip().split(' ')[0]
    numMoves = int(line.strip().split(' ')[1])
    move(direction, numMoves)

print(len(visited))