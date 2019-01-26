import math
prime = dict()
def seive():
    for i in range(1,1000011):
        prime[i] = 0
    root = math.sqrt(1000011)
    for i in range(3,1000011,2):
        if i==int(root):
            break
        if prime[i]==0:
            z = i*i
            x = i+i
            for j in range(z,1000011,x):
                prime[j] = 1
    return None
seive()
while True:
    try:
        total = []
        count = 0
        n = int(input())
        if n == 0:
            break
        else:
            for i in range(int(n),2,-1):
                if prime[i]==0:
                    if (n-i)>2:
                        n = n-i
                        print(i)
                        i = n
                        if n==2:
                            print("2")
                        if prime[n]==0:
                            print(n)
                        count = count+1
    except EOFError:
        break
