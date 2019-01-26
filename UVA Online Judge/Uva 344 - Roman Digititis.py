romanNumbers = ["c", "xc", "l", "xl", "x", "ix", "v",  "iv", "i"]
val = [100, 90, 50, 40, 10, 9, 5, 4, 1]
def toRoman(n):
    converted = []
    for i in range(9):
        d, n = divmod(n,val[i])
        for u in range(d):
            converted.append(romanNumbers[i])
    return ''.join(converted)
while True:
    try:
        m = int(input())
        if m==0:
            break
        i = int(0)
        v = int(0)
        x1 = int(0)
        l = int(0)
        c = int(0)
        for x2 in range(1,m+1):
            s = toRoman(x2)
            for x in s:
                if x=='i':
                    i = i+1
                elif x=='v':
                    v = v+1
                elif x=='x':
                    x1 = x1+1
                elif x=='l':
                    l = l+1
                elif x=='c':
                    c = c+1
        print("%d: %d i, %d v, %d x, %d l, %d c" %(m,i,v,x1,l,c))
    except EOFError:
        break
