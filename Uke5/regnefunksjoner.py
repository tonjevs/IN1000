def addisjon(a,b):
    return a + b

assert addisjon(1,4) == 5
assert addisjon(-1,-6) == -7
assert addisjon(-1,5) == 4

def substraksjon(a,b):
    return a - b

assert substraksjon(3,7) == -4
assert substraksjon(-2,-9) == 7
assert substraksjon(-7,1) == -8

def divisjon(a,b):
    return a/b

assert divisjon(6,2) == 3
assert divisjon(-5,-1) == 5
assert divisjon(-1,-2) == 0.5

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer*2.54

print(tommerTilCm(5)) #valgte 5 som argument

def skrivBeregninger():
    verdi1 = float(input("Skriv inn tall: "))
    verdi2 = float(input("Skriv inn tall: "))
    print("Resultatet av summeringen:",addisjon(verdi1,verdi2))
    print("Resultatet av substraksjonen:" , substraksjon(verdi1,verdi2))
    print("Resultatet av divisjonen:" , divisjon(verdi1, verdi2))

    print("Konverterer fra tommer til cm")
    verdi3 = float(input("Skriv inn ett tall du vil konvertere: "))
    print("Resultat" , tommerTilCm(verdi3))

skrivBeregninger()
