while True:
    try:
        n = int(input())
        lst = []
        for i in range(n):
            lst[i]
            i+=1
        for i in range(0,n+1):
            print(lst[i])
    except EOFError:
        break
