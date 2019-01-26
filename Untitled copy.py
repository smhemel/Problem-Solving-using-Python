x = int(input())
a = 0
b = 1
c = 0
for i in range(0,x):
    c = a+b
    a = b
    b = c
print(a)
    
