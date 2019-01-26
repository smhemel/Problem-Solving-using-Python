n = int(input())
s = str(input())
lista = s.split()
length = len(s)
d = length/2
for i in range(1,n+1):
    a = i*int(d)
    for j in range((int(a)-1),(int(a)-int(d))):
        print(s(j))
#uncomplete
