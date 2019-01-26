x = input().split(" ")
a,b,c=x
count = 0
while (int(a)>=3 or int(b)>=3 or int(c)>=3):
    if int(a)>=3:
        count+=1
        a = int(a)-3
    if (int(a) != 0 and int(a)<3):
        a = int(a)%3
    if int(b)>=3:
        count+=1
        b = int(b)-3
    if(int(b) != 0 and int(b)<3):
        b = int(b)%3
    if int(c)>=3:
        count+=1
        c = int(c)-3
    if(int(c) != 0 and int(c)<3):
        c = int(c)%3
while (int(a) != 0 and int(b) != 0 and int(c) != 0):
    count+=1
    a = int(a)-1
    b = int(b)-1
    c = int(c)-1
print(count)
