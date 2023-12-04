winningNums = [x.split(": ")[1].split(" | ")[0] for x in open("4.in","r").read().split("\n")]
ourNums = [x.split(": ")[1].split(" | ")[1] for x in open("4.in","r").read().split("\n")]



currentCards = [x for x in range(len(winningNums))]
allCards = 0

nextCards = {}

for i in currentCards:
    nextCards[str(i)] = 1


def getNumCards(wnums, onums,idd , nk):
    global winningNums
    global ourNums
    global nextCards
    a = nextCards
    ounums = onums.split(" ")
    while "" in ounums:
        ounums.remove("")
    winums = wnums.split(" ")
    while "" in winums:
        winums.remove("")
    oonums = [int(x) for x in ounums]
    wwnums = [int(x) for x in winums]
    c = []
    ns = 0
    for n in oonums:
        if n in wwnums:
            ns+=1
    for i in range(idd,idd+ns):
        if(not str(i+1) in a.keys()):
            a[str(i+1)] = 0
        a[str(i+1)] += nk
    return a



s = 0
for i in nextCards.keys():
    s+= nextCards[i]

print(nextCards)
while len(nextCards.keys())!=0:
    oldCards = nextCards
    nextCards = {}
    for card in oldCards.keys():
        nextCards = getNumCards(winningNums[int(card)],ourNums[int(card)],int(card), oldCards[card])
    for i in nextCards.keys():
        s+= nextCards[i]

print(s)

