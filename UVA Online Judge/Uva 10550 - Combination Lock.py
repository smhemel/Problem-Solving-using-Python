while True:
    try:
        c,c1,c2,c3 = map(int,input().split(" "))
        if c==0 and c1==0 and c2==0 and c3==0:
            break
        print("%d"%(1080+int((c-c1+40)%40 +(c2-c1+40)%40 + (c2-c3+40)%40)*9))
    except EOFError:
              break
