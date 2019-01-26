al = input().split(" ")
x,y,z = al
a = (float(x)*float(z))/2
b = 3.14159*(float(z)**2)
c = float(z)*(float(x)+float(y))/2
d = float(y)*float(y)
e = float(x)*float(y)
print("TRIANGULO: %.3f" %a)
print("CIRCULO: %.3f" %b)
print("TRAPEZIO: %.3f" %c)
print("QUADRADO: %.3f" %d)
print("RETANGULO: %.3f" %e)
