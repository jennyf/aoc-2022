inputFile = open("input", "r")
for line in inputFile:
    for i in range(len(line.strip())):
        if len(set(line[i:i+14])) == 14:
            print(i+14)
            exit()