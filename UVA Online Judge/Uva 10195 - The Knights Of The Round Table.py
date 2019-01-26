import math
while True:
    try:
        x = input().split(" ")
        a,b,c = x
        if (float(a)==0 or float(b)==0 or float(c)==0):
            print("The radius of the round table is: 0.000")
        else:
            s = (float(a)+float(b)+float(c))/2
            s1 = ((s-float(a))*(s-float(b))*(s-float(c)))/s
            r = math.sqrt(float(s1))
            print("The radius of the round table is: %.3f" %r)
    except EOFError:
        break
