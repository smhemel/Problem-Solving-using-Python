while True:
    try:
        sum = 0
        while(1):
            n = int(input())
            sum = sum + n
            if n==0:
                print(sum)
                break
    except EOFError:
        break
