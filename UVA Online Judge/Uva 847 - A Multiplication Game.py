while True:
    try:
        n = int(input())
        if(n==1):
            print("Stan wins.")
            continue
        count = 0
        while(n>1):
            count+=1
            if count%2==1:
                n = int((n+8)/9)
            else:
                n = int((n+1)/2)
        if count%2==1:
            print("Stain wins.")
        else:
            print("Ollie wins.")
    except EOFError:
        break
