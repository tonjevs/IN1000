class Gave:

    def __init__(self,gaveNavn,pris):
        self._gaveNavn = gaveNavn
        self._pris = pris

    def gavePris(self):
        return self._pris

    def gaveNavn(self):
        return self._gaveNavn

    def __str__(self):
        s = 'Gavenavn:' , gaveNavn() , 'Pris:' , gavePris
        return s

class Barn:

    def __init__(self,BarnNavn):
        self._BarnNavn = BarnNavn
        self._totVerdi = 0
        self._antGaverListe = []

    def BarnNavn(self):
        return self._BarnNavn

    def totalVerdi(self):
        return self._totVerdi

    def apneGave(self,gave):
        self._totVerdi + gave.gavePris()
        self._gaver.append(gave)

    def skrivBarn(self):
        print(self._navn + ":")
        for gave in self._gaver:
            print(gave)
        ptint("Totalverdi: " + self._totVerdi)

class Julekalender:

    def __init__(self,alleBarn,gaveFil):
        self._alleBarn = alleBarn
        self._gavefil = gaveFil
        self._kalender = []

    def nyDag(self):
        for dager in self._kalender()

    def gaveOversikt(self):
        pass

    def _lesGavefil(self):
        fil = open(self._gavefil,"r")
        self._gaveListe = []
        for linjer in fil:
            linjer.split(',').strip()
            gave = Gave(linjer[0],linjer[1])
            self._gaveListe.append(gave)
        fil.close()

    def _kalender(self):
        for dag in range(0,24):
            for gave in self._gaveOrdbok:
                dag = gave

    def _apnere(self):
        for barn in self._alleBarn:
            print(barn)

    def _nesteApner(self):


    def _dag(self):
        pass
