import math

class Monkey():
    def __init__(self, id):
        self.id = id
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def setOperation(self, operation):
        self.operator = operation.strip().split(' ')[1]
        self.operand = operation.strip().split(' ')[2]

    def setTestNumber(self, testNumber):
        self.testNumber = testNumber

    def setTestTrueMonkeyId(self, testTrueMonkeyId):
        self.testTrueMonkeyId = testTrueMonkeyId

    def setTestFalseMonkeyId(self, testFalseMonkeyId):
        self.testFalseMonkeyId = testFalseMonkeyId

    def getNewWorryLevel(self, item):
        if self.operand == 'old':
            operand = item
        else:
            operand = int(self.operand)

        if self.operator == '*':
            return math.floor(item * operand / 3)
        else:
            return math.floor((item + operand) / 3)

    def inspect(self, item):
        global activityMap
        activityMap[self.id] += 1
        newWorryLevel = self.getNewWorryLevel(item)
        if newWorryLevel % self.testNumber == 0:
            return (newWorryLevel, self.testTrueMonkeyId)
        else:
            return (newWorryLevel, self.testFalseMonkeyId)

    def __repr__(self):
        print(self.items)
        return '\n'

monkeys = []
activityMap = {}
inputFile = open("input", "r")
for line in inputFile:
    if line.startswith('Monkey'):
        id = int(line.strip().split(' ')[1][:1])
        monkeys.append(Monkey(id))
        activityMap[id] = 0
    elif 'Starting' in line:
        for item in line.split(':')[1].split(','):
            monkeys[-1].addItem(int(item.strip()))
    elif 'Operation' in line:
        monkeys[-1].setOperation(line.split('=')[1])
    elif 'Test' in line:
        monkeys[-1].setTestNumber(int(line.strip().split(' ')[-1]))
    elif 'true' in line:
        monkeys[-1].setTestTrueMonkeyId(int(line.strip().split(' ')[-1]))
    elif 'false' in line:
        monkeys[-1].setTestFalseMonkeyId(int(line.strip().split(' ')[-1]))
    else:
        next

for i in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            result = monkey.inspect(item)
            monkeys[result[1]].items.append(result[0])
        monkey.items = []

counts = list(activityMap.values())
max1 = max(counts)
counts.remove(max1)
max2 = max(counts)
print(max1 * max2)