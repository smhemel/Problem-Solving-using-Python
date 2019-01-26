a=int(input())
lx=[]
ly=[]
for i in range(a):
    x,y=map(int,input().split())
    lx.append(x)
    ly.append(y)
dist=0
mn=abs(sum(lx)-sum(ly))
op=sum(lx)
up=sum(ly)
for i in range(a):
    if abs(op-lx[i]+ly[i]-(up-ly[i]+lx[i]))>mn:
        mn=abs(op-lx[i]+ly[i]-(up-ly[i]+lx[i]))
        dist=i+1
print(dist)
