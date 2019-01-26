maxi = 0
for i in range(100):
    i+=1
    n = int(input())
    if maxi<n:
        maxi=n
        position = i
print("%d\n%d" %(maxi,position))
