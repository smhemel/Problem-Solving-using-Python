import sys

sys.stdin = open('input.txt')
while True:
    m, n = map(int, input().split())
    if not m and not n:
        break
    print (pow(m, n, 10))