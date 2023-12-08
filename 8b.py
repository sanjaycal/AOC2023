toFollow = [0 if x=="L" else 1 for x in open("8.in","r").read().split("\n\n")[0]]

instructionsAsList = [x for x in open("8.in","r").read().split("\n\n")[1].split("\n")]



insturctions = {}

for instruction in instructionsAsList:
    start = instruction[:3]
    end = (instruction[7:10],instruction[12:15])
    insturctions[start] = end


head = []

for i in insturctions.keys():
    if i[-1] == "A":
        head.append(i)

steps = 0

allHeadsZ = []

cycles = [-1 for x in head]
delay = [-1 for x in head]

cyclesStarted = [False for x in cycles]
cyclesFinished = [False for x in cycles]

slhead = len(head)

while len(allHeadsZ) != slhead:
    head = [insturctions[x][toFollow[steps%len(toFollow)]] for x in head]


    steps +=1

    for i in range(len(head)):
        if head[i][-1]=="Z" and delay[i]==-1:
            delay[i] = steps
        elif head[i][-1]=="Z":
            if not cyclesFinished[i]:
                cycles[i] = steps-delay[i]
                cyclesFinished[i] = True


    if not (-1 in delay) and not (-1 in cycles):
        break

    

    if steps%100000==0:
        print(steps)



print(cycles)
print(delay)

import math

scad = []

for x in range(len(cycles)):
    if cycles[x]==delay[x]:
        scad.append( cycles[x])


clcm = 1

for i in range(len(scad)):
    clcm = math.lcm(clcm,scad[i])

print(clcm)