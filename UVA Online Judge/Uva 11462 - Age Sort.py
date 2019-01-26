while True:
    try:
        n = int(input())
        if n==0:
            break
        for i in range(1):
            x=[int(i) for i in input().split()]
        x.sort()
        count = 0
        for i in range(n):
            count+=1
            if count==n:
                print(x[i])
                break
            else:
                print(x[i], end=" ")
    except EOFError:
        break
    
