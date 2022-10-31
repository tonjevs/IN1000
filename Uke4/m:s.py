liste = [6 , -4 , 7 , -2 , 8 , -3 , 9 , -11]

minst = liste[0]
for e in liste:
    if e < minst:
        minst = e

print(minst)

størst = liste[7]
for s in liste:
    if s > størst:
    størst = s

print(størst)
