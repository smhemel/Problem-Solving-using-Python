while True:
    try:
        n = int(input())
        ans = int(1)
        fac = list()
        for i in range(1,n+1):
            ans *=i
        length = len(str(len))
        print("%d! --" %n)
        for i in range(10):
            count = int(0)
            for l in str(ans):
                if(i==int(l)):
                    count +=1
            if(i==5):
                print()
            if(i==9):
                print("(%d)    %d" %(int(i),count))
            else:
                print("(%d)    %d    " %(int(i),count),end = "")
    except EOFError:
        break
