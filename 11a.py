data = open("11.in","r").read().split("\n")

allemptyColumns = []
allEmptyRows = []


for x in range(len(data[0])):
    allZeros = True
    for y in range(len(data)):
        if data[y][x]!=".":
            allZeros = False
    if allZeros:
        allemptyColumns.append(x)


for y in range(len(data)):
    allZeros = True
    for x in range(len(data[0])):
        if data[y][x]!=".":
            allZeros = False
    if allZeros:
        allEmptyRows.append(y)


allGalaxies = []

nya = 0

for y in range(len(data)):
    if y in allEmptyRows:
        nya+=1
    nxa = 0
    for x in range(len(data[0])):
        if x in allemptyColumns:
            nxa += 1
        if data[y][x] == "#":
            ey = y + nya
            ex = x + nxa
            allGalaxies.append([ey,ex])

out = 0

for i in range(len(allGalaxies)):
    for j in range(len(allGalaxies)):
        out += abs(allGalaxies[i][0]-allGalaxies[j][0]) + abs(allGalaxies[i][1]-allGalaxies[j][1])

print(out//2)