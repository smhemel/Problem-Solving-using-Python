store  = []
n = int(input())
l = 1
while n !=0:
    m = int(input())
    for i in range(m):
        x = int(input())
        store.append(x)
 #   store.sort()
    captain = int(m)/2
    print("Case %d: %d" %(l,store[int(captain)]))
#uncomplete
