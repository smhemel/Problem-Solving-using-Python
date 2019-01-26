m = input().split(" ")
a,b,c,d = m
x = ((float(a)*2+float(b)*3+float(c)*4+float(d)*1)/(2+3+4+1));
if (5.0<=x and x<=6.9):
    print("Media: %.1f\nAluno em exame." %x)
    n = float(input())
    z = ((x+n)/2)
    print("Nota do exame: %.1f\nAluno aprovado.\nMedia final: %.1f" %(n,z))
elif x<=4.9:
    print("Media: %.1lf\nAluno reprovado." %x)
elif x>=7.0:
    print("Media: %.1f\nAluno aprovado." %x)
