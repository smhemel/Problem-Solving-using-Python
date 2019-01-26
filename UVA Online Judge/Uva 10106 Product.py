while True:
    try:
        n = int(input())
        m = int(input())
        sum = n*m
        print(sum)
    except EOFError:
        break
