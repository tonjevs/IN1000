def ordbokfunksjon(tekstfil) :
    fil = open(tekstfil , "r") #opner tekstfilen
    for linjer in fil :
        linjer = linjer.split() #splitter linjene
        værOrdbok[linjer[0]] = float(linjer[1]) #definerer ordboken
    fil.close() #lukker
    return værOrdbok

værOrdbok = {}
ordbok = ordbokfunksjon("temperatur.txt")
print(ordbok)

def temperaturfunksjon(ordbok,filnavn) :
    fil = open(filnavn , "r")
    for linjer in fil :
        linjer = linjer.split() #splitter og definerer alle "bitene"
        måned = linjer[0]
        dato = int(linjer[1])
        temp = float(linjer[2])
        maxtemperatur = ordbok[måned]
        if temp > maxtemperatur :
            print("Ny varmerekord", måned , dato , ":" , temp , "grader Celcius. Gamle rekord var" , ordbok[måned] )
            ordbok[måned] = temp
    return ordbok
    fil.close()

temperaturfunksjon(ordbok,"dagstemperatur.txt")
print(ordbok)

def sisteprosedyre(oppdatert_ordbok,filnavn):
    fil = open(filnavn, "w")
    for element in ordbok:
        fil.write(element)
        fil.write(" ")
        fil.write(str(ordbok[element]))
        fil.write("\n") #Passer på å sette neste loop på ny linje
    fil.close()
    return ordbok
sisteprosedyre(ordbok,"nytekstfil.txt")
