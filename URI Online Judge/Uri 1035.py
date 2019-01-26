x = input().split(" ")
a,b,c,d = x
f=int(c)+int(d)
g=int(a)+int(b)
if (int(b)>int(c) and int(d)>int(a) and int(f)>int(g) and int(c)>0 and int(d)>0 and int(a)%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
