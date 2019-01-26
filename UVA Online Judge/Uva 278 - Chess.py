test = int(input())
while test!=0:
    test -= 1
    a,b,c = map(str,input().split(" "))
    if a =='r':
        print("{}".format(min(int(b),int(c))))
    elif a=='k':
        print("{}".format(int(int(int(b)*int(c)+1)/2)))
    elif a=='Q':
        print("{}".format(min(int(b),int(c))))
    else:
        t = (int(b)+1)/2
        t1 = (int(c)+1)/2
        print("{}".format(int(t)*int(t1)))
