fil = open("historie.txt" , "r")
liste = []
for linje in fil :
    split = linje.split()
    split[0] = int(split[0])
    liste.append(linje)

print(liste)
fil.close()
