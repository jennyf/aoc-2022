class Move:
    def __init__(self, name):
        self.name = name

class Rock(Move):
    def __init__(self):
        self.score = 1
        self.name = 'rock'

    def play(self, outcome):
        if outcome == 'X':
            return 3 # scissors
        elif outcome == 'Y':
            return 1 + 3 # rock + tie
        else:
            return 2 + 6 # paper + win

class Paper(Move):
    def __init__(self):
        self.score = 2
        self.name = 'paper'

    def play(self, outcome):
        if outcome == 'X':
            return 1 # rock
        elif outcome == 'Y':
            return 2 + 3 # paper + tie
        else:
            return 3 + 6 # scissors + win

class Scissors(Move):
    def __init__(self):
        self.score = 3
        self.name = 'scissors'

    def play(self, outcome):
        if outcome == 'X':
            return 2 # paper
        elif outcome == 'Y':
            return 3 + 3 # scissors + tie
        else:
            return 1 + 6 # rock + win

def parse(input):
    if input == 'A':
        return Rock()
    elif input == 'B':
        return Paper()
    else:
        return Scissors()

inputFile = open("input", "r")
sum = 0
for line in inputFile:
    parts = line.strip().split(' ')
    opponent = parse(parts[0])
    outcome = parts[1]
    sum += opponent.play(outcome)
print(sum)