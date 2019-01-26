coin = {0: int(1), 1: int(5), 2: int(10), 3: int(25), 4: int(50)}
way = dict()
way = {0: int(1)}
for i in range(0,30010):
    way[int(i+1)] = 0
for j in range(5):
    x = coin[int(j)]
    for i in range(int(x),30010):
        way[i] += way[i-coin[int(j)]]
while True:
    try:
        n = int(input())
        if way[n]==1:
            print("There is only 1 way to produce %d cents change." %n)
        else:
            print("There are %d ways to produce %d cents change." %(way[n],n))
    except EOFError:
        break
