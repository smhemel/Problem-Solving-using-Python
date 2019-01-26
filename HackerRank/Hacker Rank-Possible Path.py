from fractions import gcd
for cas in range(int(input())):
    a,b,x,y = map(int,input().split())
    print ("NO YES".split()[gcd(a,b)==gcd(x,y)])
