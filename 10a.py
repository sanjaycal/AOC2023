data = open("10.in","r").read().split("\n")

directionsdash = {"L":[0,1,"L"],"R":[0,-1,"R"]}
directionspipe = {"T":[1,0,"T"],"B":[-1,0,"B"]}
directions7 = {"L":[1,0,"T"],"B":[0,-1,"R"]}
directionsJ = {"T":[0,-1,"R"],"L":[-1,0,"B"]}
directionsL = {"T":[0,1,"L"],"R":[-1,0,"B"]}
directionsF = {"B":[0,1,"L"],"R":[1,0,"T"]}

directions = {"-":directionsdash, "|":directionspipe, "7":directions7, "J":directionsJ, "L":directionsL,"F":directionsF}


slocation = [-1,-1]
direction = [1,0,"T"]

tdistance = 0

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            slocation = [y,x]


location = [x for x in slocation]
location = [(location[x]+direction[x]) for x in range(len(location))]
direction = directions[data[location[0]][location[1]]][direction[-1]]
tdistance +=1

while location!=slocation:
    location = [location[x]+direction[x] for x in range(len(location))]
    if data[location[0]][location[1]]=="S":
        break
    direction = directions[data[location[0]][location[1]]][direction[-1]]
    tdistance +=1

print((tdistance+1)//2)