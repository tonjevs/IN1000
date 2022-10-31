flaggOrdbok = {"norge" : ["rødt", "kvitt" , "blått"],
"sverige" : ["gult" , "blått"],
"danmark" : ["rødt" , "kvitt"],
"finland" : ["blått" , "kvitt"],
"japan" : ["rødt" , "kvitt"],
"gabon" : ["grønt" , "gult" , "blått"],
"storbritannia" : ["rødt" , "kvitt" , "blått"],
"chile" : ["blått" , "kvitt" , "rødt"]}

flaggOrdbok["israel"] : ["blått" , "kvitt"]

print(flaggOrdbok)

def prosedyre():
    land = input("Skriv inn ett land fra listen over: ")
    land = land.lower()
    if land in flaggOrdbok :
        print(flaggOrdbok[land])

    else:
        print("Landet du skrev inn var ikkje på listen")

prosedyre()
