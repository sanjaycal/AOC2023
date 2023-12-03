data = [x.split(": ")[1].split("; ") for x in open("2.in","r").read().split("\n")]

s = 0


for game in data:
    mr = 0
    mg = 0
    mb = 0
    for turn in game:
        r = 0
        g = 0
        b = 0
        dice = turn.split(', ')
        for d in dice:
            if d.endswith("red"):
                r += int(d.split(" ")[0])
            if d.endswith("blue"):
                b += int(d.split(" ")[0])
            if d.endswith("green"):
                g += int(d.split(" ")[0])
        if r>mr:
            mr = r
        if g>mg:
            mg = g
        if b>mb:
            mb = b
    s += mr*mg*mb

print(s)