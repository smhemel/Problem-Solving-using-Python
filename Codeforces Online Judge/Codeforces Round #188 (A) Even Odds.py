n,k = map(int,input().split())
p=(n+1)//2
if k<=p:
    m=2*k-1
else:
    m=2*(k-p)
print(m)
