import heapq

heap = []
sum = 0
inputFile = open("input", "r")
for line in inputFile:
    if not line.strip():
        heapq.heappush(heap, sum * (-1))
        sum = 0
    else:
        sum += int(line.strip())
heapq.heappush(heap, sum * (-1))

print(heapq.heappop(heap) * -1)