n = int(input())
while(n!=0):
    n-=1
    a,b = map(int,input().split())
    if b%a==0:
        print("%d %d" %(a,b))
    else:
        print("-1")
        
