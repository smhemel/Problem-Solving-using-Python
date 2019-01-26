while True:
    try:
        x = input().split(" ")
        a,b,c = x
        if ((float(a)<(float(b)+float(c))) and (float(b)<(float(a)+float(c))) and (float(c)<(float(a)+float(b)))):
            sum=(float(a)+float(b)+float(c))
            print("Perimetro = %.1f" %sum)
        else:
            sum=((float(a)+float(b))/2*float(c))
            print("Area = %.1f" %sum)
    except EOFError:
        break
