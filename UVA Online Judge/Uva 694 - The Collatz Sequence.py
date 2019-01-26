i = 0
while True:
    try:
        x = input().split(" ")
        c,b = x
        a = int(c)
        if int(a)<=0 and int(b)<=0:
            break
        count = 0
        i += 1
        while(int(a)<=int(b)):
            count+=1
            if int(a)==1:
                break
            if int(a)%2==0:
                a = int(a)/2
            else:
                a = (3*int(a))+1
        print("Case %d: A = %d, limit = %d, number of terms = %d" %(i,int(c),int(b),count))
    except EOFError:
        break
