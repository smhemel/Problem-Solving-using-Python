t = int(input())
for i in range(t):
    n = int(input())
    j = 0
    cnt = 0
    while n>0:
        if (n&1) == 0:
            cnt += pow(2,j)
        j += 1
        n >>= 1
        print(n >> 1)
    print(cnt)

