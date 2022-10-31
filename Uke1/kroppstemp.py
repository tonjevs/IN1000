imp = input("Hva er din kroppstemperatur? ")
temp = float(imp)

if temp < 36.5 :
    print("Under normal kroppstemperatur")

elif temp > 37.5 :
    print("Over normal kroppstemperatur")

else:
    print("Normal kroppstemperatur")
