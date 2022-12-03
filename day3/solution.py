def getPriority(items):
    sum = 0
    for item in items:
        if item.islower():
            sum += ord(item) - 96
        else:
            sum += ord(item) - 64 + 26
    return sum

inputFile = open("input", "r")
sum = 0
for line in inputFile:
    line = line.strip()
    mid = int(len(line)/2)
    intersect = list(set(line[:mid]) & set(line[mid:]))
    sum += getPriority(intersect)
print(sum)