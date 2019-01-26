a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
lista = [a,b,c,d,e,f]
i = 0
count = 0
suma = 0
while (i < len(lista)):
    if (lista[i]>0):
        suma+=lista[i]
        count+=1
    i+=1
print("%d valores positivos\n%.1f" %(count,(suma/count)))
