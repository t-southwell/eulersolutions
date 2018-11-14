from math import factorial as fact
num1 = 0
tot = []
def ncr(n,r):
    x = 0
    x = fact(n)/(fact(r)*(fact(n-r)))
    return x
while num1 <= 100:
    for i in range (1,num1+1):
        z = ncr(num1, i)
        if z > 1000000:
            tot.append(z)
            i+=1
        else:
            i+=1
    num1+=1
print(len(tot))
