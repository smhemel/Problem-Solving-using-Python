import math
while True:
    try:
        n =int(input())
        for i in range(1):
            x = [int(i) for i in input().split(" ")]
        x.sort()
        for i in range(n):
            print(x[i])
    except EOFError: 
        break
