class Hytte:

    def __init__(self,navn,ant_senger,pris):
        self._navn = _navn
        self._ant_senger = ant_senger
        self._pris = pris

    def hentNavn(self):
        return self._navn

    def totPris(self,ant_personer):
        pris = self._pris/ant_personer
        return pris

    def sjekkPlass(self,ant_senger_trengt):
        for hytter in liste??
            if ant_senger_trengt >= self._ant_senger:
                return True
        return False

    def __str__(self):
        "Hyttenavn: " , hentNavn() ,
        "Antall senger: " , self._ant_senger ,
        "Pris: " , totPris()


    def __eq__(self,referanse):
        if referanse == self.verdi:
            return True
        return False

class TurPlanlegger:

    def __init__(self,filnavn1,filnavn2):
        self._filnavn1 = filnavn1
        self._filnavn2 = filnavn2

    def _hytterFraFil(self):
        hytteObrdbok = {}
        liste = []
        fil = open(self._filnavn1)
        for linjer in fil:
            biter = linjer.split()
            verdier = liste.append(int(biter[1]),float(biter[2]))
            hytteordbok.append(biter[0]) = verdier

    def _turerFraFil(self):
        pass
