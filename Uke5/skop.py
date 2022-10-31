# Først oppretter vi ein funksjon minFunksjon uten parametere.
# Deretter Definerer vi ein funksjon hvoedprogram  utan parametere.
# Så kaller vi på hovudprogram et. Vi oppretter ein variabel a med verdien 42
# deretter oppretter vi variabelen b med verdien 0, vil printer så ut verdien til
# b i terminalen og får ut 0. vi setter så b = a , altså både b og a har nå verdien
# 42. vi definerer a som minFunksjon og kaller på den. Vi setter x som en variabel innen
# området 2. Setter så en variabel c med verdien 2. Deretter printer vi ut verdien til c
# altså 2. Deretter plusser vi c med 1. Vi setter variabelen b = 10 og deretter tar vi
# b og plusser med a. a er ein udefinert verdi i dette skopet og det er heller ikkje
# definert på det globale skopet. Programmet klarer derfor ikkje printe eller returnere
# verdien for b. sidan a blei satt lik minFunksjon og den ikkje har nokon return
# verdi vil ingenting bli printa og siden b = a får vi ikkje printa ut noe anna og
# programmet e dermed stoppa med ei feilmelding. 

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b=10
        b+= a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()
