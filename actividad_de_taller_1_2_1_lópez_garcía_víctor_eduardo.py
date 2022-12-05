# -*- coding: utf-8 -*-
"""Actividad de taller 1.2.1 López García Víctor Eduardo.ipynb


Hoja 1
"""

#Cuadrado
print("Ingrese el lado del cuadrado")
L=int(input())
P= L*4 #Perimetro
A= L*L #Area
print("El perimetro del cuadrado es de: ",P)
print("El area del cuadrado es de ",A)

#Triangulo
print("Ingrese la altura del triangulo")
h=int(input())
print("Ingrese la base del triangulo")
b=int(input())
print("Ingrese el lado a del triangulo")
La=int(input())
print("Ingrese el lado b del triangulo")
Lb=int(input())
P= b+La+Lb #Perimetro
A= b*h #Area
print("El perimetro del triangulo es de: ",P)
print("El area del triangulo es de ",A)

#Rectangulo
print("Ingrese el lado A del rectangulo")
La=int(input())
print("Ingrese el lado B del rectangulo")
Lb=int(input())
P= 2*(La+Lb) #Perimetro
A= La*Lb #Area
print("El perimetro del rectangulo es de: ",P)
print("El area del rectangulo es de  ",A)

#Paralelogramo
print("Ingrese la base del Paralelogramo")
b=int(input())
print("Ingrese el lado del Paralelogramo")
La=int(input())
print("Ingrese la altura del Paralelogramo")
h=int(input())
P= 2*(La+b) #Perimetro
A= h*b #Area
print("El perimetro del Paralelogramo es de: ",P)
print("El area del Paralelogramo es de  ",A)

#Rombo
print("Ingrese el lado del rombo")
l=int(input())
print("Ingrese la diagonal a del rombo")
Da=int(input())
print("Ingrese la diagonal b del rombo")
Db=int(input())
P= 4*l #Perimetro
A= (Da*Db)/2 #Area
print("El perimetro del rombo es de: ",P)
print("El area del rombo es de  ",A)

#Cometa
print("Ingrese el lado a del cometa")
La=int(input())
print("Ingrese el lado b del cometa")
Lb=int(input())
print("Ingrese la diagonal a del cometa")
Da=int(input())
print("Ingrese la diagonal b del cometa")
Db=int(input())
P= 2*(La+Lb) #Perimetro
A= (Da*Db)/2 #Area
print("El perimetro del cometa es de: ",P)
print("El area del cometa es de  ",A)

#Trapecio
print("Ingrese el lado a del trapecio")
La=int(input())
print("Ingrese el lado b del trapecio")
Lb=int(input())
print("Ingrese la base mayor del trapecio")
B=int(input())
print("Ingrese la base menor del trapecio")
b=int(input())
print("Ingrese la altura del trapecio")
h=int(input())
P= La+Lb+B+b #Perimetro
A= (B+b)*h/2 #Area
print("El perimetro del trapecio es de: ",P)
print("El area del trapecio es de  ",A)

#Circulo
print("Ingrese el radio del circulo")
r=int(input())
Pi=3.1416
P= 2*Pi*r #Perimetro
A= Pi*(r**2) #Area
print("El perimetro del circulo es de: ",P)
print("El area del circulo es de  ",A)

#Poligono Regular
print("Ingrese el apotema del poligono regular")
a=int(input())
print("Ingrese el lado del poligono regular")
l=int(input())
print("Ingrese el numero de lados del poligono regular")
nl=int(input())
P= nl*l #Perimetro
A= (P*a)/2 #Area
print("El perimetro del poligono regular es de: ",P)
print("El area del poligono regular es de  ",A)

#Corona Circular
print("Ingrese el radio mayor de la corona circular")
R=int(input())
print("Ingrese el radio menor de la corona circular")
r=int(input())
Pi=3.1416
A= (Pi*((R**2)-(r**2))) #Area
print("El area de la corona circular es de  ",A)

#Sector Circular
print("Ingrese el radio del sector circular")
r=int(input())
print("Ingrese el angulo del sector circular")
a=int(input())
Pi=3.1416
A= (Pi*(r**2)*a)/360 #Area
print("El area del sector circular es de  ",A)

"""Hoja 2"""

#Cubo
print("Ingrese el area de un lado del cubo")
Al=int(input())
A=6*Al
V=Al**3
print("El area del cubo es de ",A) #Area
print("El volumen del cubo es de ",V) #Volumen

#Cilindro
print("Ingrese el radio la base del cilindro")
r=int(input())
print("Ingrese la altura del cilindro")
h=int(input())
Pi=3.1416
A=(Pi*2*r*(r+h)) #Area
V=(Pi*r**2*h) #Volumen
print("El area del cilindro es de ",A)
print("El volumen del cilindro es de ",V)

#Ortoedro
print("Ingrese el area del lado a del ortoedro")
a=int(input())
print("Ingrese el area del lado b del ortoedro")
b=int(input())
print("Ingrese el area del lado c del ortoedro")
c=int(input())
A=2*(a*b+a*c+b*c)
V=a*b*c
print("El area del ortoedro es de ",A) #Area
print("El volumen del ortoedro es de ",V) #Volumen

#Prisma Recto
print("Ingrese el apotema de la base del prisma recto")
a=int(input())
print("Ingrese el perimetro de la base del prisma recto")
P=int(input())
print("Ingrese el area de la base del prisma recto")
Ab=int(input())
print("Ingrese la altura del prisma recto")
h=int(input())
Pi=3.1416
A=(P*(h+a)) #Area
V=(Ab*h) #Volumen
print("El area del prisma recto es de ",A)
print("El volumen del prisma recto es de ",V)

#Cono
print("Ingrese el radio la base del cono")
r=int(input())
print("Ingrese la altura del cono")
h=int(input())
print("Ingrese la generatriz del cono")
g=int(input())
Pi=3.1416
A=(Pi*r*(r+g)) #Area
V=(Pi*r**2*h)/3 #Volumen
print("El area del cono es de ",A)
print("El volumen del cono es de ",V)

#Tronco de Cono
print("Ingrese el radio la base mayor del tronco de cono")
R=int(input())
print("Ingrese el radio la base menor del tronco de cono")
r=int(input())
print("Ingrese la altura del tronco de cono")
h=int(input())
print("Ingrese la generatriz del tronco de cono")
g=int(input())
Pi=3.1416
A=(Pi*(g*(R+r)+r**2+R**2) #Area
V=[((Pi*h)*((R**2)+(r**2)+(R*r)))/3] #Volumen
print("El area del tronco de cono es de ",A)
print("El volumen del tronco de cono es de ",V)

#Esfera
print("Ingrese el radio la base de la esfera")
r=int(input())
Pi=3.1416
A=(Pi*4*r**2) #Area
V=(Pi*4*r**2)/3 #Volumen
print("El area de la esfera es de ",A)
print("El volumen de la esfera es de ",V)

#Piramide
print("Ingrese el perimetro de la base de la piramide")
Pb=int(input())
print("Ingrese el area de la base de la piramide")
Ab=int(input())
print("Ingrese la altura de la piramide")
h=int(input())
print("Ingrese la altura del lado de la piramide")
Al=int(input())
print("Ingrese el apotema de la piramide")
a=int(input())
A=(Pb*(a+Al))/2 #Area
V=(Ab*h)/3 #Volumen
print("El area de la piramide es de ",A)
print("El volumen de la piramide es de ",V)

#Tetaedro Regular
print("Ingrese el lado del tetaedro regular")
L=int(input())
A= sqrt(3)*L**2  #Area
V= sqrt(2)*L**3/12 #Volumen
print("El area del tetaedro regular es de ",A)
print("El volumen del tetaedro regular es de ",V)

#Octaedro Regular
print("Ingrese el lado del octaedro regular")
L=int(input())
A= (2*sqrt(3)*L**2)  #Area
V= (sqrt(2)*L**3)/3 #Volumen
print("El area del octaedro regular es de ",A)
print("El volumen del octaedro regular es de ",V)

#Tronco de Piramide
print("Ingrese el perimetro de la base a del tronco de piramide")
Pba=int(input())
print("Ingrese el perimetro de la base b del tronco de piramide")
Pbb=int(input())
print("Ingrese el area de la base a del tronco de piramide")
Aba=int(input())
print("Ingrese el area de la base b del tronco de piramide")
Abb=int(input())
print("Ingrese la altura del tronco de piramide")
h=int(input())
print("Ingrese la altura del lado del tronco de piramide")
Al=int(input())
A=((Pba+Pbb)/2)Al+Aba+Abb #Area
V=((Aba+Abb+sqrt(Aba*Abb))*h)/3 #Volumen
print("El area del tronco de piramide es de ",A)
print("El volumen del tronco de piramide es de ",V)

#Casquete Esferico
print("Ingrese el radio del casquete esferico")
r=int(input())
print("Ingrese la altura del casquete esferico")
h=int(input())
Pi=3.1416
A=(2*Pi*r*h) #Area
V=(Pi*h**2*(3*r-h))/3 #Volumen
print("El area del Casquete Esferico es de ",A)
print("El volumen del Casquete Esferico de ",V)

#Huso Cuña Esferica
print("Ingrese el radio de la Cuña Esferica esferica")
r=int(input())
print("Ingrese la altura de la Cuña Esferica esferica")
h=int(input())
print("Ingrese el angulo de la Cuña Esferica esferica")
n=int(input())
Pi=3.1416
A=(4*Pi*(r**2)*n)/360 #Area
V=(4*Pi*(r**3)*n)/360*3  #Volumen
print("El area de la Cuña Esferica es de ",A)
print("El volumen de la Cuña Esferica es de ",V)

#Zona o segmento esferico
print("Ingrese el radio de la Zona o segmento esferico")
r=int(input())
print("Ingrese la altura de la Zona o segmento esferico")
h=int(input())
Pi=3.1416
A=(2*Pi*r*h) #Area
V=(Pi*h*((h**2)+(3*r**2)+(3*r**2))/6) #Volumen
print("El area de la Zona o segmento esferico es de ",A)
print("El volumen de la Zona o segmento esferico es de ",V)