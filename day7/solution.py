class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

class Directory(File):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.subdirs = []

    def addFile(self, file):
        self.files.append(file)

    def addTotalSize(self, size):
        self.totalSize = size

def cd(dir):
    global root, currentDir
    if dir == '/':
        currentDir = root
    elif dir == '..':
        currentDir = currentDir.parent
    else:
        for subdir in currentDir.subdirs:
            if subdir.name == dir:
                currentDir = subdir

def addDir(dir):
    global currentDir
    currentDir.subdirs.append(Directory(dir, currentDir))

def addFile(line):
    global currentDir
    size = int(line.split(' ')[0])
    name = line.split(' ')[1]
    currentDir.files.append(File(name, size, currentDir))

def calculateTotalSize(dir):
    global resultDirs
    sum = 0
    for f in dir.files:
        sum += f.size
    for subdir in dir.subdirs:
        sum += calculateTotalSize(subdir)
    dir.totalSize = sum
    if sum <= 100000:
        resultDirs.append(dir)
    return sum

root = Directory('/', None)
currentDir = root
resultDirs = []
inputFile = open("input", "r")
for line in inputFile:
    if line.startswith('$ cd'):
        cd(line.strip().split(' ')[2])
    elif line.startswith('$ ls'):
        next
    else:
        if line.startswith('dir'):
            addDir(line.strip().split(' ')[1])
        else:
            addFile(line.strip())

calculateTotalSize(root)

sum = 0
for dir in resultDirs:
    if dir.name != '/':
        sum += dir.totalSize
print(sum)