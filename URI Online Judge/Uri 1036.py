while True:
    try:
        import math
        x = input().split(" ")
        a,b,c = x
        d=(float(b)*float(b))-(4*float(a)*float(c))
        if(float(a)!=0):
            r1=(-float(b) + math.sqrt(abs(d)))/(2*float(a))
            r2=(-float(b) - math.sqrt(abs(d)))/(2*float(a))
        if (float(a)!=0 and float(d)>0):
            print("R1 = %.5f\nR2 = %.5f" %(r1,r2))
        else:
            print("Impossivel calcular")
    except EOFError:
        break
