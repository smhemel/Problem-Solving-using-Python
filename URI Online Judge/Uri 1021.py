a = float(input())
b=a*100
c=(b/10000)
d=(b%10000)/5000
e=((b%10000)%5000)/2000
f=(((b%10000)%5000)%2000)/1000
g=((((b%10000)%5000)%2000)%1000)/500
h=(((((b%10000)%5000)%2000)%1000)%500)/200
i=((((((b%10000)%5000)%2000)%1000)%500)%200)/100
j=(((((((b%10000)%5000)%2000)%1000)%500)%200)%100)/50
k=((((((((b%10000)%5000)%2000)%1000)%500)%200)%100)%50)/25
l=(((((((((b%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)/10
m=((((((((((b%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)%10)/5
n=(((((((((((b%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)%10)%5)/1
print("NOTAS:\n%d nota(s) de R$ 100.00\n%d nota(s) de R$ 50.00\n%d nota(s) de R$ 20.00\n%d nota(s) de R$ 10.00\n%d nota(s) de R$ 5.00\n%d nota(s) de R$ 2.00\nMOEDAS:\n%d moeda(s) de R$ 1.00\n%d moeda(s) de R$ 0.50\n%d moeda(s) de R$ 0.25\n%d moeda(s) de R$ 0.10\n%d moeda(s) de R$ 0.05\n%d moeda(s) de R$ 0.01" % (c,d,e,f,g,h,i,j,k,l,m,n))
