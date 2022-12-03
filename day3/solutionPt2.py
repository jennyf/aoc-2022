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
group = []
for line in inputFile:
    group.append(line.strip())
    if (len(group) % 3 == 0):
        intersect = list(set(group[0]) & set(group[1]) & set(group[2]))
        sum += getPriority(intersect)
        group = []
print(sum)