let = input().split(" ")
a,b,c = let
mainor = (int(a)+int(b)+abs(int(a)-int(b)))/2
z = (int(mainor)+int(c)+abs(int(mainor)-int(c)))/2
print("%d eh o maior" %z)
