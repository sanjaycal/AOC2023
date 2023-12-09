data = [[int(x) for x in y.split(" ")] for y in open("9.in","r").read().split("\n")]


def get_next(valueHistory):
    allZeros = True
    for i in valueHistory:
        if i!=0:
            allZeros = False
    if allZeros:
        return 0
    diffList = []
    for i in range(len(valueHistory)-1):
        diffList.append(valueHistory[i+1]-valueHistory[i])
    return valueHistory[-1] + get_next(diffList)

s = 0

for i in data:
    s+= get_next(i)

print(s)