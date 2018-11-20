from fractions import Fraction as fract
x = set()
for i in range(1,80001):
    for z in range(int((fract(3,7)*i)-1/i),i):
        if z/i>=3/7:
            i+=1
        else:
            print(fract(z,i))
            x.add(fract(z,i))

x = sorted(x)
print('---',x.pop(), '---')
