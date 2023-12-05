data = [x.split(":")[-1] for x in open("5.in","r").read().split("\n\n")]

def convert(n, inmap):
    cns = n
    out = []
    for mp in inmap:
        #print(f"mp:{mp}")
        ncns = []
        for zone in cns:
            if mp[1]>zone[0] and mp[0]<zone[1]:
                overlappingZone = [(mp[0] if mp[0]>zone[0] else zone[0]) +mp[2],(mp[1] if mp[1]<zone[1] else zone[1]) + mp[2]]
                out.append(overlappingZone)
                if mp[0]<zone[0] and mp[1]<zone[1]:
                    nonOverlappingZones = [[mp[1],zone[1]]]
                elif zone[0]<mp[0] and mp[1]<zone[1]:
                    nonOverlappingZones = [[zone[0],mp[0]],[mp[1],zone[1]]]
                elif zone[0]<mp[0] and zone[1]<mp[1]:
                    nonOverlappingZones = [[zone[0],mp[0]]]
                else:
                    nonOverlappingZones = []
                #print(f"nonzone{nonOverlappingZones}, zone: {zone}, mp:{mp}")
                ncns += nonOverlappingZones
            else:
                ncns.append(zone)
        cns = ncns
    out += cns
    #print(cns)
    return out


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

tseeds = []

for i in range(len(seeds)//2):
    tseeds.append([seeds[2*i],seeds[2*i]+seeds[2*i+1]])

seeds = tseeds

for inmap in maps:
    #print("")
    nseeds = convert(seeds,inmap)
    seeds = nseeds
    #print(seeds)

print(min([x[0] for x in seeds]))