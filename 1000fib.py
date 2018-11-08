num = 1
prevnum = 0
fnum = 1
x = 0
while len(str(num))<1000:
    x = prevnum + num
    prevnum = num
    num = x
    fnum+=1
    print num
    print
print
print fnum
