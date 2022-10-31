from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self,filnavn):
        fil = open(filnavn , "r")
        for linjer in fil:
            linjer = linjer.split(";")
            sang = Sang(linjer[1],linjer[0])
            self._sanger.append(sang)
        fil.close()

    def leggTilSang(self,nySang):
        self._sanger.append(nySang)

    def fjernSang(self,sang):
        self._sanger.remove(sang)

    def spillSang(self,sang):
        sang.spill()

    def spillAlle(self):
        for sanger in self._sanger:
            print(sanger)

    def finnSang(self,tittel):
        for objekter in self._sanger :
            måte = objekter.sjekkTittel(tittel)
            if måte == True:
                return objekter
        return None

    def hentArtistUtvalg(self,artistnavn):
        artistSpilleliste = []
        for linjer in self._sanger:
            måte = linjer.sjekkArtist(artistnavn)
            if måte == True:
                artistSpilleliste.append(linjer)
        return artistSpilleliste
        return None
