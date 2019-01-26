fib = dict()
def fibo():
    fib[0] = 1
    fib[1] = 2
    for i in range(2,1001):
        fib[i] = fib[i-1]+fib[i-2]
fibo()
while True:
    try:
        n = int(input())
        print(fib[n])
    except EOFError:
        break
