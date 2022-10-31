fil = open("navn.txt" , "r")
liste_hund = []
liste_person = []

for linje in fil :
    if linje[0] == "P" :
        liste_person.append(linje[2:-1])
    elif linje[0] == "H" :
        liste_hund.append(linje[2:-1])
    else :
        print("Feil i linjeformatet:\n" , linje)
fil.close()
print("Personer: " , liste_person)
print("Hunder: " , liste_hund)
