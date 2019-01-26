import math
prime = dict()
def seive():
    for i in range(1,1000000):
        prime[i] = 0
    root = math.sqrt(1000000)
    for i in range(3,1000000,2):
        if i==int(root):
            break
        if prime[i]==0:
            z = i*i
            x = i+i
            for j in range(z,1000000,x):
                prime[j] = 1
    return None
seive()
while True:
    try:
        n = int(input())
        for i in range(3,n+1,2):
            if prime[i]==0:
                print(i)
    except EOFError:
        break
