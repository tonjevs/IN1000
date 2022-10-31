#Dette programmet skal skrive datoer som en variabel, setter derfor en float for
#å lage input til ett desimaltall
inp = input("Skriv inn en dato(m.dd): ")
dato_1 = float(inp)

#Setter måneden først fordi den avgjer mest
inp = input("Skriv inn en annen dato(m.dd): ")
dato_2 = float(inp)

if dato_1 < dato_2 :
    print("Riktig rekkefølge!")

elif dato_1 > dato_2 :
    print("Feil rekkefølge!")

else :
    print("Samme dato")
