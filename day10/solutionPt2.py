def getPixel():
    global sprite, cycle
    if (cycle + 1) % 40 in sprite:
        return '#'
    else:
        return '.'

inputFile = open("input", "r")
sprite = range(1,4)
cycle = 0
output = [[]]
for line in inputFile:
    if line.strip() == 'noop':
        output[-1].append(getPixel())
        cycle += 1
        if (cycle) % 40 == 0:
            output.append([])
    else:
        V = int(line.strip().split(' ')[1])
        for i in range(2):
            output[-1].append(getPixel())
            cycle += 1
            if (cycle) % 40 == 0:
                output.append([])
        newX = sprite[0] + V
        sprite = range(newX,newX+3)

for line in output:
        print(''.join(line))