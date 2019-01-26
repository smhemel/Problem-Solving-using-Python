while True:
    try:
        n = float(input())
        m = float(input())
        ans = m**(1/n)
        print("%.f" %ans)
    except EOFError:
        break
