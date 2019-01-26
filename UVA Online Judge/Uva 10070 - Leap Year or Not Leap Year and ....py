while True:
    try:
        n = int(input())
        flag = int(1)
        if n%400==0:
            flag = 0
            print("This is leap year.")
        if n%100 !=0 and n%4==0:
           flag = 0
           print("This is leap year.")
        if n%15==0:
            flag = 0
            print("This is huluculu festival year.")
        if n%55==0:
            flag = 0
            print("This is Bulukulu festival year.")
        if flag==1:
            print("This is an ordinary year.")
        print()
    except EOFError:
        break
