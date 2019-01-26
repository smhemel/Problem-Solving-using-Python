while True:
    try:
        l = []
        used = set()
        n,m = map(int,input().split(" "))
        ans = int(n/m)
        print("{}/{} = {}.".format(n,m,int(ans)),end = '')
        n %= m
        n *= 10
        while n not in used:
            l.append(n)
            used.add(n)
            n %= m
            n *= 10
        i = 0
        result = []
        while l[i] != n:
            print("{}".format(int(l[i]/m)),end = '')
            i += 1
        print("(",end='')
        j = i
        l_length = len(l)
        while int(i)<int(l_length):
            if int(i)>=50:
                break
            print("{}".format(int(l[i]/m)),end = '')
            i += 1
        if i<l_length:
            print("...",end = '')
        print(")")
        print("   {} = number of digits in repeating cycle".format(int(l_length)-int(j)))
        print()
    except EOFError:
        break