x = 0
n = range(100,1000)
total = 0
totvals = []
while len(str(x))<4:
    for i in range(1,len(n)):
        total = x*n[i]
        if str(total) == str(total)[::-1]:
            totvals.append(total)
    x+=1
    totvals.sort()
    print totvals
