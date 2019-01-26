n = int(input())
a = 0
b = 1
for i in range(n):
    i+=1
    if n==i:
        print(a)
        break
    print(a, end=' ')
    c = a+b
    a = b
    b = c
