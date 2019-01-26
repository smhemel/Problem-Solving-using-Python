N = int(input())
A = [int(A) for A in input().strip().split(' ')]
A.reverse()
for i in range(len(A)):
    print (A[i], "", end="")
