s=raw_input().split()
n=int(s[0])
m=int(s[1])
pri=[int(x) for x in raw_input().split()]
rel=[set() for x in range(n)]
for i in range(m):
	s=raw_input().split()
	a=int(s[0])-1
	b=int(s[1])-1
	rel[a].add(b)
	rel[b].add(a)
rpta=1<<30
for i in range(n):
	for j in range(i+1,n):
		for k in range(j+1,n):
			if i in rel[j] and i in rel[k] and j in rel[k]:
				rpta=min(rpta,pri[i]+pri[j]+pri[k])
if rpta!=1<<30:
	print (rpta)
else:
	print (-1)
