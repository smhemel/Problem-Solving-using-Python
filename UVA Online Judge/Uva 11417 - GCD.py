def gcd(a,b):
    if b==0:
        return int(a)
    else:
        m = int(a)%int(b)
        return gcd(int(b),int(m))
while True:
    try:
        n = int(input())
        if n==0:
            break
        sum = 0
        for i in range(1,n+1):
            j = i+1
            for j in range(j,n+1):
                sum = sum+gcd(i,j)
        print(sum)
    except EOFError:
        break
