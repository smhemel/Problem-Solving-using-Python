x = input().split(" ")
a,b = x
if (int(a)>int(b)):
    gam=(24-int(a))+int(b)
    print("O JOGO DUROU %d HORA(S)"%gam)
elif (int(a)<int(b)):
    gam=(int(b)-int(a))
    print("O JOGO DUROU %d HORA(S)"%gam)
elif (int(a)==int(b)):
    gam=(24-int(a))+int(b)
    print("O JOGO DUROU %d HORA(S)" %gam)
