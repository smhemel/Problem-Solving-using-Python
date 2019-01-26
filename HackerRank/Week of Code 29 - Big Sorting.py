import sys
sys.stdin = open('/Users/HEMEL/Downloads/input.txt')
n = int(input())
a = list()
for i in range(n):
    a.append(int(input()))
a = sorted(a)
for l in range(n):
    print(a[l])
