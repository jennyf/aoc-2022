import ast, functools

aslist=lambda x: x if type(x)==list else [x]

def compare(a, b):
    if type(a)==type(b)==int:
        return a-b
    a,b = aslist(a), aslist(b)
    for x,y in zip(a,b):
        if (r:=compare(x,y)) != 0:
            return r
    return len(a)-len(b)

inputFile = open("input", "r")
packets = [[2], [6]]
for line in inputFile:
    if not line.isspace():
        packets.append(ast.literal_eval(line.strip()))
packets = sorted(packets, key=functools.cmp_to_key(compare))
print((packets.index([2])+1) * (packets.index([6])+1))