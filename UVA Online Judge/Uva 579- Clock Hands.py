while True:
    try:
        x = input().split(":")
        h,m = x
        if int(h)==0 and int(m)==0:
            break
        degree_h = (float(h)*30)+(float(m)/2)
        degree_m = float(m)*6
        total = abs(degree_h-degree_m)
        if total>180:
            total = 360-float(total)
        print("%.3f" %total)
    except EOFError:
        break
