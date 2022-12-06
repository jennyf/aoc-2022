inputFile = open("input", "r")
for line in inputFile:
    for i in range(len(line.strip())):
        if len(set(line[i:i+4])) == 4:
            print(i+4)
            exit()