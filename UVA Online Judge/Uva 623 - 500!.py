'''my_list = dict()
def recur_factorial(n):
    my_list[1] = 1
    for i in range(2,n+1):
        my_list[i] = my_list[i-1]*i 
z = 500
m = recur_factorial(z)'''
while True:
    try:
        x = int(input())
        suma = 1
        for i in range(1,x+1):
            suma = int(suma)*i
        print("%d!" %x)
        print(suma)
    except EOFError:
        break
