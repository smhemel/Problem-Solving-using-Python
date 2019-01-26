import math
n = 1000
marked = {}
list1 = []
for i in range(2, int(math.sqrt(n))):
    if not marked.get(i):
        for x in range(i * i, n, i):
            marked[x] = True

for i in range(2, n):
    if not marked.get(i):
        list1.append(i)
n = int(input())
for i in range(0,n):
    print(list1[i])
    
