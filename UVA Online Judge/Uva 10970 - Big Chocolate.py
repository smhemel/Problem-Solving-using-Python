while True:
    try:
        x = input().split(" ")
        a,b = x
        c = (int(a)*int(b))
        print(int(c)-1)
    except EOFError:
        break
