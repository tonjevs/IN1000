#I denne oppgaven skal du lage en quiz ved bruk av liste og løkker.
svar = ["Svart" , "Mandel" , "Peter Jackson"]
    print("Hei! Velkommen")
    ja_nei = input("Er du klar for quiz(ja/nei)? ")

    if ja_nei == "ja" :
        poeng = 0
        print("Da starter vi: ")
        print("NB: Alle svar har stor forbokstav")

        spørs1 = input("Hvilken farge har giraffens tunge: ")
        if spørs1 == svar[0]
            print("Korrekt")
        if spørs1 == svar[0] :
                        poeng = poeng + 1
                else :
                    print("Det var dessverre feil. Giraffens tunge er svart...")

                spørs2 = input("Hvilken type nøtt er marsipan laget av: ")
                if spørs2 == svar[1] :
                    print("Korrekt")
                    if spørs2 == svar[1] :
                        poeng = poeng + 1
                else :
                    print("Det var dessverre feil. Det er mandel som blir brukt for å lage marsipan...")

                spørs3 = input("Hvem registrerte Lord of the Rings filmene: ")
                if spørs3 == svar[2] :
                    print("Korrekt")
                    if spørs3 == svar[2] :
                        poeng = poeng + 1
                else:
                    print("Det var dessverre feil. Det var Peter Jackson som registrerte Lord of the Rings")

                print("Du fikk" , poeng , "/ 3")

            elif ja_nei == "nei" :
                print("Okay...")
            else :
                print("Input ikke mulig")
