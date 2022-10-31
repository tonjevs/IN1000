inp = input("Hvor høy er du: ")
høyde = int(inp)

if høyde < 140 :
    print("Du er lav")

elif høyde > 140 and høyde < 190 :
    print("Du er middels")

else:
    print("Du er høy")
