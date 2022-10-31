#I denne oppgaven skal du lage en quiz ved bruk av liste og løkker.
def quizprosedyre():
    svar = ["Blå" , "Nei" , "Hjernen"]
    print("Hei! Velkommen")
    ja_nei = input("Er du klar for quiz(ja/nei)? ")

    if ja_nei == "ja" :
        poeng = 0
        print("Da starter vi: ")
        print("NB: Alle svar har stor forbokstav")

        spørs1 = input("Hvilken farge er det på solnedganen på Mars: ")
        if spørs1 == svar[0] :
            print("Korrekt")
            if spørs1 == svar[0] :
                poeng = poeng + 1
        else :
            print("Det var dessverre feil. Solnedgangen på mars er 'Blå''...")

        spørs2 = input("Kan vi nyse i søvne(Ja/Nei): ")
        if spørs2 == svar[1] :
            print("Korrekt")
            if spørs2 == svar[1] :
                poeng = poeng + 1
        else :
            print("Det var dessverre feil. 'Nei' vi kan ikke nye i søvne...")

        spørs3 = input("Hvilket organ i menneskekroppen har mest fett: ")
        if spørs3 == svar[2] :
            print("Korrekt")
            if spørs3 == svar[2] :
                poeng = poeng + 1
        else:
            print("Det var dessverre feil. Det er 'Hjernen' som har mest fett")

        print("Du fikk" , poeng , "/ 3")

    elif ja_nei == "nei" :
        print("Okay...")
    else :
        print("Input ikke mulig")

    fortsette = input("vil du spille på nytt(ja/nei): ")
    if fortsette == "ja" :
        quizprosedyre()
    elif fortsette == "nei" :
        print("Ok, ha en fin dag videre")
    else:
        print("Umulig input!")

quizprosedyre()
