test = int(input())
while test!=0:
    test -=1
    n = int(input())
    ans = int(1)
    for i in range(2,n+1):
        ans *= i
    print(ans)
