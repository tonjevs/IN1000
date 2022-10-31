def funksjon(tall1 , tall2):
    summer = (tall1 + tall2)
    print(tall1 , "+" , tall2 , "er" , summer)

funksjon(4 , 5)
funksjon(1 , 3)

def tellForekomst(minTekst , minBokstav):
    teller = 0
    for tegn in minTekst:
        if tegn == minBokstav:
            teller += 1
    print("Det er" , teller , minBokstav, "-er i" , minTekst)

minTekst = input("Skriv inn ett ord: ")
minBokstav = input("Skriv inn en bokstav: ")
tellForekomst(minTekst , minBokstav)
