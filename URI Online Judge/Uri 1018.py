a = int(input())
suma = (a/100);
sub  = (a%100)/50;
mul  = ((a%100)%50)/20;
w    = (((a%100)%50)%20)/10;
x    = ((((a%100)%50)%20)%10)/5;
y    = (((((a%100)%50)%20)%10)%5)/2;
z    = ((((((a%100)%50)%20)%10)%5)%2)/1;
print("%d\n%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00" % (a,suma,sub,mul,w,x,y,z))
