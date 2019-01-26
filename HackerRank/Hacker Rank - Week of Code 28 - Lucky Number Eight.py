'''import itertools
n = int(input())
s = input()
com = [list(itertools.combinations(s,x)) for x in range(1,len(s)+1)]
com = [''.join(e) for e in sum(com,[])]
k=[]
for l in com:
    k.append(l)
ans = 0
for no in k:
    if int(no)%8==0:
        ans=ans+1
print(ans%1000000007)'''


n = int(input())
m = input()
r = int(1)
length = len(m)
for i in range(int(length)):
    r = (r*10 + int(m[i]) - 48) % 8
print(r)
