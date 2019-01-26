n = int(input())
i = 1
while(n>0):
    x = input().split("/")
    y = input().split("/")
    day,month,year = x
    day1,month1,year1 = y
    age = int(year)-int(year1)
    if int(month) < int(month1):
        age-=1
    if int(month)==int(month1):
        if int(day)<int(day1):
            age-=1
    if age<0:
        print("Case #%d: Invalid birth date" %i)
    elif age>130:
        print("Case #%d: Check birth date" %i)
    else:
        print("Case #%d: %d" %(i,age))
    i+=1
    n-=1
