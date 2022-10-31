#lager ordboken
matplanOrdbok = {"Kari" : ("frokostblanding" , "yoghurt og musli" , "spaghetti") ,
"Karl" : ("brødskiver" , "havregryn" , "brennsnut") ,
"Mona" : ("pannekaker" , "ostesmørbrød" , "hamburger")
}

#definerer prosedyren
def matplanprosedyre():
    print("Kari , Karl og Mona")
    person = input("Skriv inn ett navn og få deres matplan: ")
    person.lower() #setter navnet i små bokstaver
    if person in matplanOrdbok :
        print(matplanOrdbok[person])
    else:
        print("Personen er dessverre ikke registrert som beboer")

matplanprosedyre()

#a) mengde kan bruke liste også men mengder tar mindre tid, og dersom man skriver ett brukernamn med en feil to ganger
    #så vil det fortsatt kun bli registrert en gang
#b) ordbok fordi da kan man søke på navnet og finne scoren deira
#c) liste fordi man kun treng navn, mengder ville sletta folk med like navn og satt dei en gang
#d) ordbok fordi da kan man søke på navn og finne kva dei er alergisk mot
