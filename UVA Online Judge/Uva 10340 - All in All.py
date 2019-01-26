while True:
    try:
        x = input().split(' ')
        a , b = x
        m = len(str(a))
        n = len(str(b))
        count = 0
        for i in range(n):
            if count >n:
                break
            if(a[i]==b[count]):
                count+=1
        if count==m:
            print("Yes")
        else:
            print("No")
    except EOFError:
        break
