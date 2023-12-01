data = open("1.in","r").read().split("\n")

def get_number(strn):
    strn = strn.replace('one', 'one1one')
    strn = strn.replace('two', 'two2two')
    strn = strn.replace('three', 'three3three')
    strn = strn.replace('four', 'four4four')
    strn = strn.replace('five', 'five5five')
    strn = strn.replace('six', 'six6six')
    strn = strn.replace('seven', 'seven7seven')
    strn = strn.replace('eight', 'eight8eight')
    strn = strn.replace('nine', 'nine9nine')
    fn = -1
    ln = 0
    nums = [str(x) for x in range(10)]
    cs = ""
    for c in strn:
        if c in nums:
            ln = c
            if fn==-1:
                fn=c
            cs = ""
    return int(fn+ln)


ns = 0

for i in data:
    ns += get_number(i)

print(ns)