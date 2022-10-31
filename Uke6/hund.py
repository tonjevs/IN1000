class Hund :
    def __init__(self,alder,vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    def hentalder(self,alder):
        return self._alder

    def hentvekt(self,vekt):
        return self._vekt

    def spring(self):
        if self._metthet <= 5:
            self._metthet -= 1

    def spis(self):
        heltall = int(input("Skriv inn ett heltall:"))
        if self._metthet + heltall >= 7 :
            self._vekt = self._vekt + 1
        return self._vekt
