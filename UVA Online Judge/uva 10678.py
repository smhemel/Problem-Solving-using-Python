import math
n = int(input())
pi = math.atan(1)*4
while (n!=0):
    a,b = map(int,input().split(" "))
    area = float(pi)*(b/2) * math.sqrt((b/2)*(b/2)-(a/2)*(a/2))
    print("%.3f"%(area))
    n-=1
