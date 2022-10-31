liste = []
tall = liste.append(int(input("Skriv inn ett tall: ")))

while tall != 0:
    tall = (int(input("Skriv inn ett tall: ")))
    liste.append(tall) #legger til tall i listen
print(liste)

for tall in liste: #kjører at for alle tall i listen skal dei printe ut verdiene
    print(tall)

minSum = 0
for tall in liste:
    minSum = minSum + tall
print("Summen av tallene er:" , minSum)

liste.sort() #sorterer listen fra lavest til høyest verdi slik det blir enkelt å finne høgest/lavest verdi

minst = liste[0] #siden vi sorterte er alltid indeks 0 den minste
for tall in liste:
    if tall < minst:
        tall = minst
print(minst , "er det minste tallet i listen")

størst = liste[(len(liste) - 1)] #her må vi heller sette lengden av listen -1 som den siste indeksen
for tall in liste:
    if tall > størst:
        tall = størst
print(størst, "er det største tallet i listen")
