store = dict()
n = int(input())
t = 1
while(n!=0):
    value = -1
    store.clear()
    for i in range(10):
        x = input().split(" ")
        s,m = x
        if(int(m)>value):
            value = int(m)
            store.clear()
            store[i] = str(s)
        elif int(m)==int(value):
            store[i] = str(s)
    print("Case #%d:" %int(t))
    length = len(store)
    for i in range(length):
        print(store[i])
    n-=1
