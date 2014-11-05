"""
Projektowanie i Programowanie w GiS - zadanie 4
Paulina Sosnowska
grupa 4, GiK I MSU

Zadanie 4 - Duplikaty
"""
def duplikat(dane):
    duplikat=list(set(dane))
    return duplikat
dane_wejsciowe=['kot','pies','chomik','kot','pies','pies','wydra','okon']
print "Wynik:"
print duplikat(dane_wejsciowe)    
