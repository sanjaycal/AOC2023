data = [x.split(":")[-1] for x in open("5.in","r").read().split("\n\n")]

def convert(n, inmap):
    outn = n
    for mp in inmap:
        if mp[0]<=n<mp[1]:
            outn += mp[2]
    return outn


def getMap(instr):
    if instr[0]=="\n":
        instr = instr[1:]
    maps = [[int(y) for y in x.split(" ")] for x in [x for x in instr.split("\n")]]
    nmaps = []
    for m in maps:
        nmaps.append([m[1],m[1]+m[2],m[0]-m[1]])
    return nmaps

maps = []

for i in data[1:]:
    maps.append(getMap(i))

seeds = data[0]

seeds = [int(x) for x in seeds[1:].split(" ")]

for inmap in maps:
    nseeds = []
    for seed in seeds:
        nseeds.append(convert(seed,inmap))
    seeds = nseeds
    print(seeds)

print(min(nseeds))