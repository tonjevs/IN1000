from spillbrett import Spillbrett
def main():

    rader = int(input("Hvor mange rader: "))
    kolonner = int(input("Hvor mange kolonner: ")) #lag bruker taste inn

    brett = Spillbrett(rader,kolonner) #lager brettet
    brett.tegnBrett() #tegner første generasjon av brettet

    brukerinput = ''
    while brukerinput != "q" :
        brukerinput = input("Trykk c for neste generasjon, q for å avslutte programmet: ")

        if brukerinput == "c":
            brett.oppdatering()
            brett.tegnBrett() #oppdaterer brettet så lenge brukeren vil det

main()
