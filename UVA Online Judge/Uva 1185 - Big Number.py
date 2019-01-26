from math import *
fac = dict()
fac[1] = 1
for i in range(2,10000001):
    fac[i] = fac[i-1] + log10(i)
n = int(input())
while n!=0:
    n -= 1
    m = int(input())
    print(int(fac[m]))
