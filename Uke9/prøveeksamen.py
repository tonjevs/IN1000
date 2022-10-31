from random import randint
class Emne:
    def __init__(self,emnekode,regstud,rettere):
        self._emnekode = emnekode
        self._regstud = {}
        self._rettere = []

    def administrer(self):
        print(
            "O: Ny oblig F: Frist ute, start retting L: Lag eksamensliste A: Avslutt"
            )
        svar = input("Hva vil du gjøre: ").lower().strip()

        while svar != "a":
            if svar == "o":
                self._opprettOblig()

            elif svar == "f":
                self._startRetting()

            elif svar == "l":
                self._skrivEksamensListe()

            else :
                print("Ugyldig input, prøv på nytt...")

    def _opprettOblig(self):
        obligid = None
        for tall in range(0,3):
            n = str(random.range(0,10000))
            frist = int(input("Skriv inn frist for oblig(ddmmåå): "))
            obligid = obligid+n
        Oblig(n,frist)

    def _startretting(self):
        dato = int(input("Hva er dagens dato: "))
        if klarforRetting(dato):
            print("Alle obliger rettet...")
        else :
            besvarelser = hentBesvarelser()
            fordelRetting(besvarelser,self._rettere)

    def _skrivEksamensListe(self):
        eksamensliste = []
        if antGodkjent:
            eksamensliste.append(student)

class Student:
    def __init__(self,brukernavn,fullt_navn):
        self._brukernavn = brukernavn
        self._fullt_navn = fullt_navn
        resultatordbok = {}

    def registrer(self,obligid,resultat):
        resultatordbok[obligid] = int(resultat)

    def altGodkjent(self,antObliger):
        self._antObliger = antObliger
        for resultat in resultatordbok:
            if resultatordbok[resultat] != 1:
                antObliger -= 1
                return False
        print(antObliger , bestått)
        return True

class Retter:
    def __init__(self,retter_brukernavn):
        self._retter_brukernavn = retter_brukernavn

    def vurder(self,filnavn):
        return 1

class Oblig:
    def __init__(self,obligid,leveringsfrist):
        self._obligid = obligid
        self._leveringsfrist = leveringsfrist
        self._obligrettet = True

    def klarForRetting(self,dagensdato):
        if leveringsfrist < dagensdato :
            if self._obligrettet:
                return True
        else:
            return False

    def hentBesvarelser(self):
        studentbesvarelseordbok = {}
        fil = open("student1.txt" , "r")
        resultat = self._vurder(fil)
        studentbesvarelseordbok[self._brukernavn] = resultat

    def fordelRetting(self,ordbok,liste):
        antobliger = len(ordbok)
        for studenter in ordbok:
            verdi = self.vurder(studenter)
            self._studentbesvarelsesordbok[studenter] = verdi
            studenter = True

        antobliger = antelever - len(liste)

        return self._studentbesvarelsesordbo
