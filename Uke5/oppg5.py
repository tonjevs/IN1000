#Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil
#(som du lager selv og leverer sammen med de andre filene) der hver linje beskriver
#et navn på et mål og selve målet i tommer. Formatet vil se slik ut:
#Skulderbredde 4 Halsvidde 3.2 Livvidde 10
#Hint​: du kan bruke funksjonen .​split()​ for å gjøre dette.
#La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og
#returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål
#og benytter seg av ​tommerTilCm​ som du skrev tidligere for å skrive ut målene i centimeter

fil = open("skredder.txt" , "r")
ordbok = {}
for linje in fil :
    linje = linje.split()
    biter = linje[0]
    ordbok[biter] = float(linje[1])
print(ordbok)


def tommerTilCm(antallTommer):
    return antallTommer*2.54 #ganger og returnerer verdien for omgjeringa

for biter in ordbok:
    print(biter,  ":" , tommerTilCm(ordbok[biter])) #printer ut for hver linje

fil.close()
