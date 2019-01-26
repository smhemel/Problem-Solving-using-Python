x = input().split(" ")
a,b = x
if (int(b)%int(a)==0):
    print("Sao Multiplos")
elif (int(a)%int(b)==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
