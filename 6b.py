t = open("6.in","r").read().split("\n")[0].split(":")[1].replace(" ","")
d = open("6.in","r").read().split("\n")[1].split(":")[1].replace(" ","")

import math

times = int(t)
distances = int(d)

print(times)
print(distances)

def calculate_distance(holdTime, TotalTime):
    return holdTime*(TotalTime-holdTime)

def getMargin(time, distance):
    out1 = 0
    for i in range(time):
        if calculate_distance(i,time)>distance:
            out1 = i
            break
    out2 = 0
    for i in range(time,0,-1):
        if calculate_distance(i,time)>distance:
            out2 = i
            break
    print(out1)
    print(out2)
    return out2-out1 + 1

o = 1

o *= getMargin(times,distances)

print(o)

#x^2-tx+d = 0