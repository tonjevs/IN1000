#Programmet skal få ett svar for deretter å bestemme en respons
print("Velkommen til min butikk! ")
svar = input("Kunne du tenke deg en brus? (ja/nei) ")

#Dersom input svaret var ja/nei vil responsen være satt
if svar == "ja" :
    print("Her har du en burs!")

elif svar == "nei" :
    print("Den er grei")

#Om bruker satte inn ett ugyldig svar vil responsen bli :
else :
    print("Det forstod jeg ikke helt")
