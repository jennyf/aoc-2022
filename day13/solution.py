import ast

# helpers copied from tinyurl.com/2p844afb
aslist=lambda x: x if type(x)==list else [x]

def rcmp(a,b):
    if type(a)==type(b)==int:
        return a-b
    a,b = aslist(a), aslist(b)
    for x,y in zip(a,b):
        if (r:=rcmp(x,y)) != 0:
            return r
    return len(a)-len(b)

inputFile = open("input", "r")
pairCount = 1
rightOrderPairs = []
pairs = []
for line in inputFile:
    if line.isspace():
        if rcmp(pairs[0], pairs[1]) < 0:
            rightOrderPairs.append(pairCount)
        pairs = []
        pairCount += 1
    else:
        pairs.append(ast.literal_eval(line.strip()))
print(sum(rightOrderPairs))