b = int(input())
p = int(input())
m = int(input())
def modulas(b,p,m):
    if p==1:
        return 1
    if(p%2==0):
        return (mod(b,p%2,m)*mod(b,p/2,m))%m
    return (mod(b,p-1,m)*(b%m))%m
print(modulas(b,p,m))
