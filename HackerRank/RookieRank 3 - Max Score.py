t = int(input())
for _ in range(t):
    t1,t2 = input().strip().split(' ')
    if t1[-2:]==t2[-2:]:
        if t1[:2]=="12":
            t1 = "".join(["00",t1[2:]])
        if t2[:2]=="12":
            t2 = "".join(["00",t2[2:]])
        if t1<t2:
            print ("First")
        else:
            print ("Second")
    else:
        if t1[-2:]=="AM":
            print ("First")
        else:
            print ("Second")
