import decimal
import math
import sys
decimal.getcontext().prec = 10100000
#sys.stdin = open('/Users/HEMEL/Desktop/input.txt')
n = int(input())
for _ in range(n):
    a, b = map(str, input().strip().split())
    check = int(0)
    for i in range(len(a)):
        if (a[i]=='1' or a[i]=='2' or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='8' or a[i]=='9'):
            check = 1
            break
    for i in range(len(b)):
        if(b[i]=='1' or b[i]=='2' or b[i]=='3' or b[i]=='4' or b[i]=='5' or b[i]=='6' or b[i]=='7' or b[i]=='8' or b[i]=='9'):
            check = 1
            break
    if (a=='.' and b=='.') or (a==b and check==0):
        print("0.0")
        continue
    if a=='.':
        s = str(decimal.Decimal(b)).rstrip('0')
        if s[-1] == '.':
            print(s + '0')
        else:
            print (s)
            continue
    if b=='.':
        s = str(decimal.Decimal(a)).rstrip('0')
        if s[-1] == '.':
            print (s + '0')
        else:
            print (s)
            continue
    if (float(a)<0 and float(b)>0 and float(abs(float(a)))==float(abs(float(b)))) or (float(a)>0 and float(b)<0 and float(abs(float(a)))==float(abs(float(b)))):
        print("0.0")
        continue
    s = str(decimal.Decimal(a) + decimal.Decimal(b)).rstrip('0')
    a = 0
    b = 0
    if s[-1] == '.':
        print (s + '0')
    else:
        print (s)
