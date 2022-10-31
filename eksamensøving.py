class Hytte:

    def __init__(self,navn,antSenger,pris):
        self._navn = navn
        self._antSenger = antSenger
        self._pris = pris

    def hentNavn(self):
        return self._navn

    def totPris(self,antPers):
        return self._pris / antPers

    def sjekkPlass(self,trengteSenger):
        if trengteSenger <= self._antSenger:
            return True
        return False

    def __str__(self):
        return 'Hyttas navn: ' , self._navn
        'Hytta har' , self._antSenger , 'senger'
        'Pris:' , self._pris

    def __eq__(self,refHytte):
        return self._navn == refHytte.hentNavn()

class Tur:

    def __init__(self,hytteRefListe,beskrivelse):
        self._hytteRefListe = hytteRefListe
        self._beskrivelse = beskrivelse

    def skrivTur(self):
        print(self._beskrivelse)
        for hytter in self._hytteRefListe:
            print("Turen går gjennom" , hytter)

    def sjekkPrisPlass(self,personer,maksBelop):
        self._personer = personer
        self._maksBelop = maksBelop

        for hytter in self._hytteRefListe:
            if self._maksBelop <= hytte.totPris(self._personer):
                if hytte.sjekkPlass(self._personer):
                    return True

class Turplanlegger:

    def __init__(self,hytteFil,turFil):
        self._hytteFil = hyttefil
        self._turFil = turFil

    def _hytteFraFil(self,filnavn):
        hytter = {}
        fil = open(filnavn)
        for linjer in fil:
            linjer = linjer.split().strip()
            hytte = Hytte(linjer[0],int(linjer[1]),float(linjer[2])
            hytter[linjer[1]] = hytte
        fil.close()

        return hytter

    def _turerFraFil(self,filnavn):
        fil = open(filnavn)
        self._turliste = []
        linjer = fil.readline().strip()
        while linjer != "" :
            linje2 = fil.readline()
            hyttenavn = linje2.split()
            liste = [hyttenavn]
            tur = Tur(liste,linjer)
            self._turliste = self._turliste.append(tur)
        fil.close()
        return self._turliste

    def finnTurer(self,antPers,maksBelop,antDager):
        for turer in self._turliste:
            if turer.hentAntHytter() <= int(antDager):
                if int(antPers) <= turer.sjekkPrisPlass(int(antPers),float(maksBelop):
                    turer.skrivTur()

def hovudprogram():
    turer = Turplanlegger("hytter.txt" , "turer.txt")
    tur = turer.finnTurer(7,7000,5)
    print(tur)

hovudprogram():
