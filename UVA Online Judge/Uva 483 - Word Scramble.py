while True:
    try:
        n = str(input())
        check = 0
        length = len(n)
        for i in range(0,length+1):
            if n[i]==' ':
                for j in range((i-1),check):
                    print(n[j], end='')
                    j-=1
                print(' ')
                check  = i
        for k in range((length-1),check):
            print(n[k], end='')
            k-=1
        print("\n")
    except EOFError:
        break
