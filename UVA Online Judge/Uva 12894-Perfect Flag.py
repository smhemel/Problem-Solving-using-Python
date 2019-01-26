n = int(input())
while(n>0):
    m = input().split(' ')
    x,y,x1,y1,z,z1,r = m
    length = int(x1)-int(x)
    width = int(y1)-int(y)
    if (5*width == 3*length) and (length == 5*int(r)) and (20*(int(z)-int(x)) == 9*length) and (2*(int(z1)-int(y)) == width):
        print("YES")
    else:
        print("NO")
    n-=1
