liste1 = ["3" , "7" , "9"]
liste1.append("5")
print(liste1)
print(liste1[0])
print(liste1[2])

liste2 = []
liste2.append(input("Vennligst skriv inn ett navn: "))
liste2.append(input("Vennligst skriv inn ett navn: "))
liste2.append(input("Vennligst skriv inn ett navn: "))
liste2.append(input("Vennligst skriv inn ett navn: "))
print(liste2)

if "Tonje" in liste2 :
    print("Du husket meg!")

else:
    print("Glemte du meg?")

summen = 3+7+9+5
produktet = 3*7*9*5
print(summen)
print(produktet)

liste3 = [summen , produktet]
print(liste3)

liste4 = liste1 + liste3
print(liste4)
liste4.pop(5) and liste4.pop(4)
print(liste4)
