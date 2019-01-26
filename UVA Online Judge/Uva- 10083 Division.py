while True:
    try:
        x = input().split(" ")
        a,b,c =  x
        m = (int(a)**int(b))-1
        n = (int(a)**int(c))-1
        suma = m//n
        number = suma
        Count = 0
        while(number > 0):
            number = number // 10
            Count = Count + 1
            if Count>100:
                break
        if (m%n==0 and Count<=100):
            print("(%d^%d-1)/(%d^%d-1) %d" % (int(a),int(b),int(a),int(c),int(suma)))
        else:
            print("(%d^%d-1)/(%d^%d-1) is not an integer with less than 100 digits." %(int(a),int(b),int(a),int(c)))
    except EOFError:
        break
