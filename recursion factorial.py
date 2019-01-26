def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
while True:
    try:
        n = int(input())
        if n>13:
            print("Underflow!")
        elif n<8:
            print("Overflow!")
        else:
            m = recur_factorial(n)
            print(int(m))
    except EOFError:
        break
