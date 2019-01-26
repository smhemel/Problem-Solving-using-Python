x = input().split(" ")
a,b,c = x
count = 0
while ((int(a)>0 and int(b)>0) or (int(a)>0 and int(c)>0) or (int(b)>0 and int(c)>0)):
    if (int(a)==0 and int(b)==0) or (int(a)==0 and int(c)==0) or (int(b)==0 and int(c)==0):
        break
    if (int(a)>0 and int(b)>0) or (int(a)>0 and int(c)>0) or (int(b)>0 and int(c)>0) or (int(a)>0 and int(b)>0 and int(c)>0):
        if (int(a)>0 and int(b)>0 and int(c)>0):
            count+=1
            a = int(a)-1
            b = int(b)-1
            c = int(c)-1
        if((int(a)==1 and int(b)==1) or (int(a)==1 and int(c)==1) or (int(b)==1 and int(c)==1)) or ((int(a)==0 and int(b)==0) or (int(a)==0 and int(c)==0) or (int(b)==0 and int(c)==0)):
            break
        if ((int(a)>0 and int(b)>0) or (int(a)>0 and int(c)>0) or (int(b)>0 and int(c)>0)) and (int(a==0 or int(b)==0 or int(c)==0)):
            if (int(a)>int(b)) or (int(a)>int(c)):
                a = int(a)-2
                b = int(b)-1
                c = int(c)-1
                count+=1
            if (int(a)==int(b) or int(a)==int(c) or int(b)==int(c)):
                break;
            if (int(b)>int(a)) or (int(b)>int(c)):
                b = int(b)-2
                a = int(a)-1
                c = int(c)-1
                count+=1
            if (int(a)==int(b) or int(a)==int(c) or int(b)==int(c)):
                break;
            if (int(c)>int(a)) or (int(c)>int(b)):
                c = int(c)-2
                a = int(a)-1
                b = int(b)-1
                count+=1
            if (int(a)==int(b) or int(a)==int(c) or int(b)==int(c)):
                break;
print(count)
