x = int(input())
i = 1
while x!=0:
    suma = 0
    n = int(input())
    m = int(input())
    if n%2==0:
        n = n+1
    for l in range(n,m+1,2):
        suma = suma + l
    print("Case %d: %d" %(i,suma))
    x-=1
    i+=1
