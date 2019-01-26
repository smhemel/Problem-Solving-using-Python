F = dict()
G = dict() 
def gx(x):
    z = (F[x-1]+G[x-1] )*(F[x-1]+G[x-1]-4)+12*G[x-1]+7
    return z
def fx(x):
    l = 2*(F[x-1]+G[x-1]-1)*(F[x-1]+G[x-1]-3) + 12*F[x-1] - 13
    return l
n = int(input())
F[0] = 2
G[0] = 1
for i in range(1,1000000):
    F[i] = fx(i)%1000000007
    G[i] = gx(i)%1000000007
for i in range(1,n+1):
    m = int(input())
    print("Case %d: %d %d" %(i,F[m],G[m]))
