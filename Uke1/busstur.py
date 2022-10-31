passasjerer = 0


inp = input("Stasjon 1: Hvor mange skal på? ")
nye = int(inp)

if passasjerer + nye >= 30 :
    print("Beklager" , passasjerer + nye  - 30 , "må vente på neste buss")
    passasjerer = 30
else:
    passasjerer += nye
    print("Stig ombord" , nye)
    

inp = input("Stasjon 2: Hvor mange skal på? ")
nye = int(inp)

if passasjerer + nye >= 30 :
    print("Beklager" , passasjerer + nye - 30 , "må vente på neste buss")
    passasjerer = 30
else:
    passasjerer += nye
    print("Stig ombord" , nye)


inp = input("Stasjon 3: Hvor mange skal på? ")
nye = int(inp)

if passasjerer + nye >= 30 :
    print("Beklager" , passasjerer + nye - 30 , "må vente på neste buss")
    passasjerer = 30
else:
    passasjerer += nye
    print("Stig ombord" , nye)
