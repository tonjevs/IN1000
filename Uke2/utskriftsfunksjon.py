#Her lager jeg ett program som spør om brukerens navn og hvor du kommer fra
#tre ganger
#Definerer prosedyren
def prosedyre() :
    navn = input("Skriv inn ett navn: ")
    bosted = input("Hvor kommer du fra? ")

    print("Hei" , navn , "! Du er fra" , bosted)

#kaller på prosedyren tre ganger
prosedyre()
prosedyre()
prosedyre()
