x = 1
while x<1000:
    for k in range(1,1000):
        for i in range(1,1000):
            if (((x**2)+(i**2))==k**2) and (x+i+k==1000):
                print x, i, k
                exit()
    x+=1
