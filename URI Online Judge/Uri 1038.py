while True:
    try:
        x = input().split(" ")
        a,b = x
        if int(a)==1:
            sum=int(b)*4.00
            print("Total: R$ %.2f" %sum)
        elif int(a)==2:
            sum=int(b)*4.50
            print("Total: R$ %.2f" %sum)
        elif int(a)==3:
            sum=int(b)*5.00
            print("Total: R$ %.2f" %sum)
        elif int(a)==4:
            sum=int(b)*2.00
            print("Total: R$ %.2f"%sum)
        elif int(a)==5:
            sum=int(b)*1.50
            print("Total: R$ %.2f"%sum)
    except EOFError:
        break
