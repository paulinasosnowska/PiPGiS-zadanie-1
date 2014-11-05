"""
Projektowanie i Programowanie w GiS - zadanie 3
Paulina Sosnowska
grupa 4, GiK I MSU

Zadanie 3 - Funkcja kwadratowa i miejsce zerowe
"""
from math import sqrt
#Funkcja kwadratowa
def funkcja_kwadratowa(a,b,c,x):
    y=a*(x**2)+b*x+c 
    return y

print "Wartosc funkcji kwadratowej wynosi:"
print (funkcja_kwadratowa(2,3,1,4))
    
#Miejsce zerowe
def miejsce_zerowe(a,b,c):  
    delta=b**2*a*c 
   
    if delta>0:
        x1=(-b-sqrt(delta))/2*a
        x2=(-b+sqrt(delta))/2*a
        return x1, x2
  
    elif delta==0:
        x0=-b/(2*a)
        return x0
    else:
        return None
print "Miejsca zerowe:"
print (miejsce_zerowe(2,4,2))

#dodatkowe zadanie
for i in xrange(-10,10):
    print "Funkcja kwadratowa w zadanym przedziale wynosi:"
    print funkcja_kwadratowa(1,1,1,i)