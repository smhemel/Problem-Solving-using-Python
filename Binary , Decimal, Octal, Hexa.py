#Decimal To Binary
for i in range(21):
    print("{0:>2} in binary is {0:>b}".format(i))
print("=" * 40)
#Decimal To Hexadecimal
for i in range(21):
    print("{0:>2} in binary is {0:>x}".format(i))
x,y = 0x20,0xa
print("{} {}".format(x,y))
print("=" * 40)
number = []
for i in range(15,-1,-1):
    number.append(2**i)
n = int(input("Please Enter a number: "))
printing = False
for p in number:
    bit = n//p
    if bit !=0:
        printing = True
    if printing:
        print(n//p,end='')
    n %= p
