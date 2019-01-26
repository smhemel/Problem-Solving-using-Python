from fractions import gcd
n = int(input())
for i in range(n):
    s = input().split(" / ")
    a = int(s[0])
    b = int(s[1])
    c = int(gcd(a,b))
    print("%d / %d"%(a//c,b//c))
    
