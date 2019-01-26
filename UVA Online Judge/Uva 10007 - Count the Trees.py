def fac(a,b):
    ans = int(1)
    for i in range(int(b+1),int(a+1)):
        ans = ans*i
    return ans
while True:
    try:
        n = int(input())
        if n==0:
            break
        x = fac((2*n),(n+1))
        print(x)
    except EOFError:
        break
