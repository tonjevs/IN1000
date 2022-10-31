class Motorsykkel :

    def __init__(self,merke,regestreringsnummer,kilometerstand) :
        self._merke = merke
        self._regestreringsnummer = regestreringsnummer
        self._kilometerstand = kilometerstand

    def kjor(self,km):
        self._start = 0
        self._tur = self._start + km
        self._kilometerstand += self._tur

    def hentKilometerstand(self):
        return self._kilometerstand

    def skrivUt(self):
        print("Merket:" , self._merke , "Regestreringsnummer:" , self._regestreringsnummer , "Kilometerstand:" , self._kilometerstand)
