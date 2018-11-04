import math
s = []
bound = input("Enter a number:")
for num in range (2, bound):
    isPrime = True
    for x in range (2, int(math.sqrt(num))+1):
        #print x
        if num%x == 0:
            isPrime = False
    if isPrime:
        s.append(num)
        print num
        #print num
print sum(s)
#print s
