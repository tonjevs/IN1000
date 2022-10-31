#I dette programmet lagde jeg ett program som spør trivia til brukeren
print("Hei! Velkommen til trivia, vil du delta?")
ja_nei = input("ja/nei: ")

#setter alle prosessene under denne if-en fordi da kjøres ikke alle dei andre
#prosessane 
if ja_nei == "ja" :

    print("Fantastisk, da starter vi!")
    print("Fornamn og etternamn i store bokstaver")
    spørs1 = input("Hvem oppfant sexdukker: ")

    if spørs1 == "Adolf Hitler" :
        print("Korrekt!")
    else :
        print("Det var Adolf Hitler")

    spørs2 = input("Kan ekkorn dø av fallskader? (ja/nei): ")
    if spørs2 == "nei" :
        print("Korrekt!")
    else :
        print("Uten andre hinder kan ekkorn ikkje dø fra fallskader")

    spørs3 = input("Hvor langt var det lengste hoppet utført av  en katt(Waffle the Warrior cat): ")
    print("heltallcm")

    if spørs3 == "213cm" :
        print("Korrekt!")
    else :
        print("Hoppet var 213 cm og var utført av waffle the warrior cat")

    print("Takk for at du deltok")

elif ja_nei == "nei" :
    print("Ok wow, your loss")

else :
    print("Kunne ikkje forstå svar, prøv igjen")
