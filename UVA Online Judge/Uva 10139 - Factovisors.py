my_list = dict()
def recur_factorial(n):
    my_list[0] = 1
    my_list[1] = 1
    for i in range(2,n+1):
        my_list[i] = my_list[i-1]*i 
z = 2147483650
m = recur_factorial(z)
while True:
    try:
        x,y = map(int,input().split(' '))
        if (x==0 and y==1) or (x==0 and y==0) or (x==1 and y==1) or (x==1 and y==0):
            print("%d divide %d!" %(y,x))
            continue
        elif my_list[x]%y==0:
            print("%d divides %d!"%(y,x))
        else:
            print("%d does not divide %d!" %(y,x))
    except EOFError:
        break
