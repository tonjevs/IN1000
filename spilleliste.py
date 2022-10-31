from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self,filnavn):
        self._filnavn = filnavn
        open(self._filnavn , "r")
        for linjer in filnavn :
            linjer = linje.strip().split(";")
            self._sanger.append(linjer[0])
            self._filnavn.close()

    def leggTilSang(self,nySang):
        self._nysang = nySang
        self._sanger.append(self._nySang)

    def fjernSang(self,sang):
        self._sang = sang
        self._sanger.pop(sang)

    def spillSang(self,sang):
        sang.spill()

    def spillAlle(self):
        for sanger in self._sanger:
            sang = Sang(sanger)
            sang.spill()

    def finnSang(self,tittel):
        self._tittel = tittel
        for sanger in self._sanger:
            if self._tittel in self._sanger:
                return self._tittel
            else:
                return None

    def hentArtistUtvalgt(self,artistnavn):
        self._artistnavn = artistnavn
        for linjer in self._sanger:
            if self._artistnavn in self._sanger:
                return linjer
