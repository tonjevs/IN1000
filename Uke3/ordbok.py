#lager ordlisten
matvareOrdbok = {"melk" : 14.90 ,
"brød" : 24.90 ,
"yoghurt" : 12.90 ,
"pizza" : 39.90
}

print(matvareOrdbok)

vare1 = input("Skriv inn en matvare: ")
pris1 = float(input(("Skriv inn pris på varen: ")))
vare2 = input("Skriv inn en matvare: ")
pris2 = float(input(("Skriv inn pris på varen: ")))

#setter nøkkelverdiene lik verdiene
matvareOrdbok[vare1] = pris1
matvareOrdbok[vare2] = pris2
print(matvareOrdbok)
