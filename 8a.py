toFollow = [0 if x=="L" else 1 for x in open("8.in","r").read().split("\n\n")[0]]

instructionsAsList = [x for x in open("8.in","r").read().split("\n\n")[1].split("\n")]



insturctions = {}

for instruction in instructionsAsList:
    start = instruction[:3]
    end = (instruction[7:10],instruction[12:15])
    insturctions[start] = end


head = "AAA"
steps = 0

while head != "ZZZ":
    head = insturctions[head][toFollow[steps%len(toFollow)]]
    steps +=1

print(steps)
