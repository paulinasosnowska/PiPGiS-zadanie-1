"""
Projektowanie i Programowanie w GiS - zadanie 1
Paulina Sosnowska
grupa 4, GiK I MSU

Zadanie 1 - "Fizz Buzz"
"""
def fizz_buzz(n):
    liczby = range(1,n)
    for i in liczby:
        if i%3 == 0 and i%5 == 0:
            print "Fizz Buzz"
        elif i%5 == 0:
            print "Buzz"
        elif i%3 == 0:
            print "Fizz"
        else:
            print i 
print (fizz_buzz(50))
    