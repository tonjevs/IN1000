steder = []
brukerinput = steder.append(input("Skriv inn feriedestinasjon: ")) #legger til brukerinput i tillaget liste

for bruker_input in steder:
    if len(steder) < 5 : #lager en loop til lengden av listen er 5
        bruker_input = steder.append(input("Skriv inn feriedestinasjon: "))

klesplagg = []
brukerinput = klesplagg.append(input("Skriv inn klesplagg: "))

for bruker_input in klesplagg:
    if len(klesplagg) < 5 :
        bruker_input = klesplagg.append(input("Skriv inn klesplagg: "))

avreisedato = []
brukerinput = avreisedato.append(float(input("Skriv inn avreisedato(d.mm): ")))

for bruker_input in avreisedato:
    if len(avreisedato) < 5 :
        bruker_input = avreisedato.append(float(input("Skriv inn avreisedato(d.mm) ")))

reiseplan = [steder , klesplagg , avreisedato] #samler en liste av lister

for lister in reiseplan:
    print(lister) #gjør bruker klar over brukers output valg

i1 = int(input("Skriv inn ønsket liste via tall(0-2): ")) #gjør bruker klar over "indeksregler"
i2 = int(input("Skriv inn ønsket verdi via tall(0-4): "))

if 0 <= i1 <= len(reiseplan)-1 :
    if 0 <= i2 <= len(reiseplan[i1])-1 :
        print(reiseplan[i1][i2])
else:
    print("Ugyldig input!")
