hands = [x.split(" ") for x in open("7.in","r").read().split("\n")]

types = ["5OAK","4OAK","FH","3OAK","2P","1P","HC"]

cards = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")

def getType(hand):
    h = {}
    for ct in cards:
        h[ct] = 0
    for i in hand:
        h[i] += 1

    hv = list(h.values())
    nhv = []
    for i in hv:
        if i != 0:
            nhv.append(i)
    hv = nhv
    hv = sorted(hv)
    if hv == [5]:
        return 0
    elif hv == [1,4]:
        return 1
    elif hv==[2,3]:
        return 2
    elif hv==[1,1,3]:
        return 3
    elif hv == [1,2,2]:
        return 4
    elif hv == [1,1,1,2]:
        return 5
    elif hv == [1,1,1,1,1]:
        return 6
    else:
        print(hand)


def checkofHandAisGreater(a,b):
    handa = a[0]
    handb = b[0]
    ta = getType(handa)
    tb = getType(handb)
    if ta<tb:
        return True
    elif tb<ta:
        return False
    for i in range(5):
        if cards.index(handa[i])<cards.index(handb[i]):
            return True
        if cards.index(handa[i])>cards.index(handb[i]):
            return False


mins = []
s = 0
c = 1

for i in range(len(hands)):
    d = hands[0]
    pp = 0
    while d in mins:
        d = hands[pp]
        pp+=1
    for hand in hands[1:]:
        if (not (hand in mins)) and checkofHandAisGreater(d,hand):
            d= hand
    mins.append(d)
    s += c*int(d[1])
    c+=1

print(s)
        