data = open("1.in","r").read().split("\n")

def get_number(strn):
    fn = -1
    ln = 0
    nums = [str(x) for x in range(10)]
    for c in strn:
        if c in nums:
            ln = c
            if fn==-1:
                fn=c
    return int(fn+ln)


ns = 0

for i in data:
    ns += get_number(i)

print(ns)