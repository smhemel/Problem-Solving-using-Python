a = str(input())
b = str(input())
i=0
if(len(a)>len(b)):
    m = len(a)
    if(i==9):
        i+=1
    while (i<int(m)):
        if (i>(len(b)-1)):
            print(a[i])
        else:
            print(b[i], end='')
            print(a[i])
        i+=1
else:
    m = len(b)
    if(i==9):
        i+=1
    while (i<m):
        if (i>(len(a)-1)):
            print(b[i])
        else:
            print(b[i], end='')
            print(a[i])
        i+=1

    
    
