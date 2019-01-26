import sys
numTest = int(input())
for itertest in range(numTest):
    a, b = input().strip().split()
    total = int(a[::-1]) + int(b[::-1])
    print (str(total)[::-1].lstrip('0'))
