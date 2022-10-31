class Sang :
    def __init__(self,_artist,_tittel) :
        self._tittel = _tittel
        self._artist = _artist

    def spill(self) :
        print(Sang(self._artist,self._tittel))

    def __str__(self):
        return f'Spiller: {self._tittel} av {self._artist}'

    def sjekkArtist(self,navn) :
        navn = navn.lower().split()
        for ord in navn:
            if ord in self._artist.lower().split() :
                return True
        return False

    def sjekkTittel(self,tittel):
        for tittel in tittel.lower().split() :
            if tittel in self._tittel.lower().split() :
                return True
        return False

    def sjekkArtistOgTittel(self,artist,tittel) :
        for tittel in tittel.lower().split():
            if tittel in self._tittel.lower().split():
                for artist in artist.split():
                    if artist in self._artist.split():
                        return True
        return False
