import itertools
import time
import math
start_time = time.time()
x = 0
divs = set()
for i in itertools.count():
    print(x+i)
    x=x+i
    for z in range(1, int(math.sqrt(x))):
        if x%z == 0:
            divs.add(z)
            divs.add(int(x/z))
        z+=1
    print(divs)
    if len(divs)>500:
        print('---',divs,'---')
        print(x)
        print("Runtime: %s seconds" % (time.time() - start_time))
        quit()
    divs.clear()
    i+=1
