data = [x.split(": ")[1].split("; ") for x in open("2.in","r").read().split("\n")]

s = 0

gns =  [int(x.split(": ")[0].split("Game ")[-1]) for x in open("2.in","r").read().split("\n")]

c = 0

for game in data:
    legal = True
    for turn in game:
        r = 12
        g = 13
        b = 14
        dice = turn.split(', ')
        for d in dice:
            if d.endswith("red"):
                r -= int(d.split(" ")[0])
            if d.endswith("blue"):
                b -= int(d.split(" ")[0])
            if d.endswith("green"):
                g -= int(d.split(" ")[0])
        if r<0 or g<0 or b<0:
            legal = False
    s += gns[c] if legal else 0
    c+=1

print(s)