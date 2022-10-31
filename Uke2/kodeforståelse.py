#Jeg tror ikke denne koden er gyldig ettersom at det er ett plusstegn mellom
#b og "Hei". Resten virker som at det kan gå.
#I starten gjer man om tekstverdien om til en tallverdi gjennom int og
#etter det tester man heltallet mot en annen tallverdi.

a = input("Tast inn ett heltall: ")
b = int(a)

if b < 10 :
    print (b , "Hei")

#Når vi kjører koden vil den klare å lese fram til print.
#Den vil ha problemer ettersom at det står b + "Hei". Problemet blir at
#+ "adderer" eller "legger sammen" sammen to int verdier. Sidan "Hei" er en
#String eller str() vil den ikkje kunne legge sammen dette. Om man i stedenfor
#hadde puttet ett , mellom dei to verdiene hadde programmet fungert. 
