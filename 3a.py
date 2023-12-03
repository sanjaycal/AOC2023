data = open("3.in","r").read().split("\n")

nums = []
symbols = []


y = 0
for i in data:
    x = 0
    cn = ""
    for c in i:
        if c!=".":
            if c in [str(x) for x in list(range(10))]:
                cn += c
            else:
                symbols.append([x,y,c])
                if cn!="":
                    allPoses = []
                    for j in range(x-len(cn),x):
                        allPoses.append([j,y])
                    nums.append([allPoses,int(cn),len(cn)])
                    cn = ""
        else:
            if cn!="":
                allPoses = []
                for j in range(x-len(cn),x):
                    allPoses.append([j,y])
                nums.append([allPoses,int(cn),len(cn)])
                cn = ""
        x+=1
    if cn!="":
        allPoses = []
        for j in range(x-len(cn),x):
            allPoses.append([j,y])
        nums.append([allPoses,int(cn),len(cn)])
        cn = ""
    y+=1

s = 0

print(len(nums))

for num in nums:
    include = False
    for symbol in symbols:
        for pos in num[0]:
            if pos[0]-1 <= symbol[0]  <=pos[0]+1 and pos[1]-1 <= symbol[1]  <=pos[1]+1:
                include = True
    if include:
        s+=num[1]

print(s)