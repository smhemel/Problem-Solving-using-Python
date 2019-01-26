n = int(input())
i = 1
while n !=0:
    a,b,c = map(int, input().split(" "))
    if a<=20 and b<=20 and c<=20:
        print("Case %d: good" %i)
    else:
        print("Case %d: bad" %i)
    n-=1
    i+=1
