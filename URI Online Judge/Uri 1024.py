while True:
    try:
        a = int(input())
        for j in range(a):
            x = str(input())
            z = x[::-1]
            length = len(z)
            n = 0
            m = int(length/2)
            list = z
            for i in z:
                if((i>='A' and i<='Z') or (i>='a' and i<='z')):
                    list[i].append(chr(ord(i) + 3))
                    
            for l in range(m,length):
                list[l].append(chr(ord(l) - 1))
            print(list)
    except EOFError:
        break
