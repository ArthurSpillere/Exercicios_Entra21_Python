x1, x2=input().split()
y1, y2=input().split()
x1, x2=float(x1), float(x2)
y1, y2=float(y1), float(y2)
distancia=((x1-y1)**2)+((x2-y2)**2)
resultado=distancia**(1/2)
print('{:.4f}'.format(resultado))

