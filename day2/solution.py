class Move:
    def __init__(self, name):
        self.name = name

class Rock(Move):
    def __init__(self):
        self.score = 1
        self.name = 'rock'

    def play(self, move):
        if move.name == 'rock':
            return 3
        elif move.name == 'paper':
            return 0
        else:
            return 6

class Paper(Move):
    def __init__(self):
        self.score = 2
        self.name = 'paper'

    def play(self, move):
        if move.name == 'rock':
            return 6
        elif move.name == 'paper':
            return 3
        else:
            return 0

class Scissors(Move):
    def __init__(self):
        self.score = 3
        self.name = 'scissors'

    def play(self, move):
        if move.name == 'rock':
            return 0
        elif move.name == 'paper':
            return 6
        else:
            return 3

def parse(input):
    if input == 'A' or input == 'X':
        return Rock()
    elif input == 'B' or input == 'Y':
        return Paper()
    else:
        return Scissors()

inputFile = open("input", "r")
sum = 0
for line in inputFile:
    parts = line.strip().split(' ')
    opponent = parse(parts[0])
    mine = parse(parts[1])
    sum += mine.score + mine.play(opponent)
print(sum)