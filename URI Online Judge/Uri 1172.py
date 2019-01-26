list1 = []
for i in range(0,10):
    x = int(input())
    list1.append(x)
for i in range(0,10):
    if list1[i]<=0:
        print("X[%d] = 1" %i)
    else:
        print("X[%d] = %d" %(i,list1[i]))
