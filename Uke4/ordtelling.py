def ordlengde():
    ord = input("Skriv inn et ord: ")
    print(ord , "har" , len(ord) , "bokstaver i seg")
ordlengde()

setningsordbok = {}
def setningslengde():
    setning = input("Skriv inn en setning: ")
    setning = setning.split() #splitter ord inn i verdier og legger til liste
    setning = [ord.lower() for ord in setning] #.lower() slik at like ord med ulik inputmåte har samme "verdi"

    for ord in setning:
        if ord in setningsordbok:
             setningsordbok[ord] = setningsordbok[ord] + 1 #adderer en for hvert ord med samme verdi i if-sjekk
        else:
            setningsordbok[ord] = 1

    print("Det er" , len(setning) , "ord i setningen")
    for ord in setningsordbok:
        print(ord, ": forekommer" , setningsordbok[ord] , "gang/er i setningen")

setningslengde()
