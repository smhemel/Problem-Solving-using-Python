N = int(input())
total = 0
for i in range(N):
    row = input().split()
    total += int(row[i])-int(row[-(i+1)])
print(abs(total))


#2
size = input()
matrix = []

for _ in xrange(size):
    row = map(int, raw_input().split())
    matrix.append(row)
s1, s2 = 0, 0

for i in xrange(size):
    s1 += matrix[i][i]
    s2 += matrix[-i-1][i]

print abs(s1 - s2)
