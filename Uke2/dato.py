#I beguynnelsen av programmet setter jeg en spilt som deler dei to variablene
dato1d, dato1m = input("Skriv inn en dato i to heltall (12 10): ").split()
dato2d, dato2m = input("Skriv inn en annen dato i heltall (04 03): ").split()

#Først skjekker programmet om måneden er større/mindre/den samme
if dato1m < dato2m :
    print("Riktig rekkefølge!")

elif dato1m > dato2m :
    print("Feil rekkefølge!")

#Om måneden er den samme vil den skjekke for dager
elif dato1m == dato2m :
    if dato1d < dato2d :
        print("Riktig rekkefølge!")
    elif dato1d > dato2d :
        print("Feil rekkefølge")

#Om ingenting annet passer vil programmet anta og skrive:
    else :
        print("Samme dato!")
