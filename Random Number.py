from random import *
while True:
    try:
        n = int(input())
        if n==0:
            break
        print(random(1,n))
    except EOFError:
        break
