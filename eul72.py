from fractions import Fraction as fract
x = set()
for i in range(100,1,-1):
    for z in range(i-1,0, -1):
        if z/i in x:
            z-=1
        else:
            x.add(z/i)
            print(fract(z,i))
print(len(x))#1 to 8 should give len 21
