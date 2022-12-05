import re

def parseInitialState(initialLines):
    stacks = []
    stackCountLine = initialLines.pop().strip()
    stackCount = len(re.split('\s+', stackCountLine))
    for i in range(stackCount):
        stacks.append([])
    while len(initialLines) > 0:
        stackLine = initialLines.pop()
        for i in range(stackCount):
            if stackLine[i * 4] != ' ':
                stacks[i].append(stackLine[i * 4 + 1])
    return stacks

def moveCrates(stacks, line):
    p = re.compile(r'move (?P<numMoves>\d+) from (?P<fromStack>\d+) to (?P<toStack>\d+)')
    m = p.search(line)
    for i in range(int(m.group('numMoves'))):
        stacks[int(m.group('toStack'))-1].append(stacks[int(m.group('fromStack'))-1].pop())
    return stacks

inputFile = open("input", "r")
initialLines = []
stacks = []
startTurns = False
for line in inputFile:
    if line.isspace():
        startTurns = True
        stacks = parseInitialState(initialLines)
    elif startTurns:
        stacks = moveCrates(stacks, line.strip())
    else:
        initialLines.append(line)

result = ''
for stack in stacks:
    if (len(stack) > 0):
        result += stack.pop()
print(result)