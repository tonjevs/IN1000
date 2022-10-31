def billetkjøp():
    alder = int(input("Skriv inn din alder: "))
    billettpris = 0

    if alder <= 17:
        print("Du må betale 30 kr" )

    elif alder > 17:
        print("Du må betale 50 kr")

    elif alder >= 63:
        print("Du må betale 35 kr")

billetkjøp()
billetkjøp()
billetkjøp()
#Ja det er noe galt med denne prosedyren. Sidan vi setter første elif som
#"dersom alder større enn 17", vil alle aldere over 17 bli registrert som
#at de må betale 50 kr. Prosedyren vil derfor avslutte der og ikkje gå videre
#til siste elif. For å løse problemet kan vi sette ett intervall mellom 17 og 63
#på første elif
