def convert(number,b2):
    res = int(int(number)%int(b2))
    div =int(int(number)/int(b2))
    r = int(1)
    while div!=0:
        r = int(r)*10
        res = (int(div%int(b2))*r)+int(res)
        div = int(div/int(b2))
    return res
while True:
    try:
        b1, b2, n = input().split()
    except:
        break
    try:
        number = int(n, base = int(b1))
        print(number)
        number2 = convert(number,b2)
        print ('%s base %s = %d base %s' % (n, b1, number2, b2))
    except:
        print ('%s is an illegal base %s number' % (n, b1))
