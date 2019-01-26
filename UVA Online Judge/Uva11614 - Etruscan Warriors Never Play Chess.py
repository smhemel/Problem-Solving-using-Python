import math
a = int(input())
while a>0:
    n = int(input())
    m = (math.sqrt(1+8*n)-1)/2
    print(int(m))
    a-=1
