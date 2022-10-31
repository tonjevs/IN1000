UiOordbok = {}

def lagBrukernavn():
    navn = input("Skriv inn for- og etternavn: ")
    navn = navn.lower()
    navn = navn.split(" ")# setter det i små bokstaver og splitter
    brukernavn = navn[0] + navn[1][0] #siden tekst er strenger definerer vi brukernavnet slik
    print("Brukernavn: "+ brukernavn)
    return brukernavn

def lagEpost(brukernavn,adresse):
    epost = (brukernavn + "@" + adresse)
    print(epost)
    return epost

def printEpost(brukernavn,adresse):
    lagEpost(brukernavn,adresse) #kaller lag epost
    print(UiOordbok)
    return UiOordbok

def program():
    prosedyresvar = input("Skriv inn i/p/s: i = (nye brukere), p = (print ut eksisterende brukere), s = (stans program): ")

    while prosedyresvar != "s" : #kjører løkken så lenge programmet ikke er s
        while prosedyresvar == "i" :
            brukernavn = lagBrukernavn()
            adresse = input("Hva er epostadressen din: ")
            epost = lagEpost(brukernavn,adresse)
            UiOordbok[brukernavn] = adresse
            prosedyresvar = input("Skriv inn i(nye brukere)/p(print ut eksisterende brukere)/s(stans program): ")

        while prosedyresvar == "p" :
            printEpost(brukernavn,UiOordbok[brukernavn])
            prosedyresvar = input("Skriv inn i(nye brukere)/p(print ut eksisterende brukere)/s(stans program): ")

    if prosedyresvar == "s" : #avslutter programmet ved s
        print("Program avsluttet...")

program() # kaller programmet
