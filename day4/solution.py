def doesRangeFullyContain(range1, range2):
    return range2.start in range1 and range2[-1] in range1

def doesRangeContain(range1, range2):
    return range2.start in range1 or range2[-1] in range1

inputFile = open("input", "r")
countPt1 = 0
countPt2 = 0
for line in inputFile:
    ranges = line.strip().split(',')
    range1Parts = ranges[0].split('-')
    range2Parts = ranges[1].split('-')
    range1 = range(int(range1Parts[0]), int(range1Parts[1])+1)
    range2 = range(int(range2Parts[0]), int(range2Parts[1])+1)
    if doesRangeFullyContain(range1, range2) or doesRangeFullyContain(range2, range1):
        countPt1 += 1
    if doesRangeContain(range1, range2) or doesRangeContain(range2, range1):
        countPt2 += 1
print(countPt1)
print(countPt2)