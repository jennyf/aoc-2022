inputFile = open("input", "r")
X = 1
cycle = 0
sum = 0
for line in inputFile:
    if line.strip() == 'noop':
        if (cycle + 21) % 40 == 0:
            sum += (cycle + 1) * X
        cycle += 1
    else:
        if (cycle + 22) % 40 == 0 or (cycle + 21) % 40 == 0:
            gap = 2 if cycle % 2 == 0 else 1
            sum += (cycle + gap) * X
        V = int(line.strip().split(' ')[1])
        cycle += 2
        X += V
print(sum)