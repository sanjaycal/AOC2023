winningNums = [x.split(": ")[1].split(" | ")[0] for x in open("4.in","r").read().split("\n")]
ourNums = [x.split(": ")[1].split(" | ")[1] for x in open("4.in","r").read().split("\n")]


s = 0

for card in range(len(winningNums)):
    ounums = ourNums[card].split(" ")
    while "" in ounums:
        ounums.remove("")
    winums = winningNums[card].split(" ")
    while "" in winums:
        winums.remove("")
    onums = [int(x) for x in ounums]
    wnums = [int(x) for x in winums]
    c = 0
    for n in onums:
        if n in wnums:
            c+=1
    if c>0:
        print(c)
        s += 2**(c-1)

print(s)