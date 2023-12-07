t = open("6.in","r").read().split("\n")[0].split(":")[1].split(" ")
d = open("6.in","r").read().split("\n")[1].split(":")[1].split(" ")

times = []
distances = []

for time in t:
    if time!="":
        times.append(int(time))


for time in d:
    if time!="":
        distances.append(int(time))

print(distances)

def calculate_distance(holdTime, TotalTime):
    return holdTime*(TotalTime-holdTime)

def getMargin(time, distance):
    out = 0
    for i in range(time+1):
        if calculate_distance(i,time)>distance:
            out+=1
    return out

o = 1

for race in range(len(times)):
    o *= getMargin(times[race],distances[race])

print(o)
