inp = input("Skriv inn ett tall: ")
tall = int(inp)

#Spør kvifor vi definerer tall = int(imp)

if tall < 10 :
    print("Mindre enn 10")

elif tall < 20 and tall > 10 :
    print("Mellom 10 og 20")

elif tall == 10 or tall == 20 :
    print("Tallet er" , tall)

elif tall > 20 :
    print("Større enn 20")
