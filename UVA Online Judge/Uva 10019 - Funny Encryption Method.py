def hex(n):
    c = 0
    while int(n)!=0:
      s = int(n)%10
      n = int(n)/10
      if s==0:
          c+=0
      elif s==1 or s==2 or s==4 or s==8:
          c+=1
      elif s==3 or s==5 or s==6 or s==9:
          c+=2
      elif s==7:
          c+=3
    return c
test  = int(input())
while test!=0:
    count = 0
    n = int(input())
    i = n
    while int(i)!=0:
        if int(i)%2!=0:
            count+=1
        i/=2
        if int(i)==0:
            break
    print(count, end=" ")
    x = hex(n)
    print(x)
    test-=1
    
